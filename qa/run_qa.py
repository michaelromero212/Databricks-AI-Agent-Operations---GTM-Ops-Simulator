"""
QA Test Runner for AI Agent
Executes test cases and validates agent behavior
"""
import json
import sys
import os
from datetime import datetime
from pathlib import Path

# Add parent directory to path to import agent
sys.path.insert(0, str(Path(__file__).parent.parent / "agent"))

from agent import GTMAgent


class QARunner:
    """QA test runner for AI agent"""
    
    def __init__(self, test_cases_file: str):
        """
        Initialize QA runner
        
        Args:
            test_cases_file: Path to test cases JSON file
        """
        self.test_cases_file = test_cases_file
        self.agent = GTMAgent()
        self.results = []
        
    def load_test_cases(self):
        """Load test cases from JSON file"""
        with open(self.test_cases_file, 'r') as f:
            return json.load(f)
    
    def run_test_case(self, test_case: dict) -> dict:
        """
        Run a single test case
        
        Args:
            test_case: Test case definition
            
        Returns:
            Test result dict
        """
        test_id = test_case["test_id"]
        print(f"\nRunning {test_id}: {test_case['description']}")
        
        # Execute agent task
        result = self.agent.process_task(
            task_type=test_case["task_type"],
            user_id="qa_runner",
            **test_case["input"]
        )
        
        # Validate result
        response_lower = result["response"].lower()
        abstained = result["abstained"]
        
        # Check if abstention behavior matches expectation
        abstention_correct = abstained == test_case["should_abstain"]
        
        # Check if expected elements are present
        elements_found = []
        elements_missing = []
        
        for element in test_case["expected_elements"]:
            if element.lower() in response_lower:
                elements_found.append(element)
            else:
                elements_missing.append(element)
        
        # Determine pass/fail
        passed = abstention_correct and len(elements_missing) == 0
        
        test_result = {
            "test_id": test_id,
            "description": test_case["description"],
            "task_type": test_case["task_type"],
            "priority": test_case["priority"],
            "passed": passed,
            "abstention_correct": abstention_correct,
            "expected_abstain": test_case["should_abstain"],
            "actual_abstain": abstained,
            "elements_found": elements_found,
            "elements_missing": elements_missing,
            "response_preview": result["response"][:200] + "..." if len(result["response"]) > 200 else result["response"],
            "resolution_time": result["resolution_time_seconds"],
            "confidence": result["confidence"],
            "timestamp": datetime.now().isoformat()
        }
        
        # Print result
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"  {status}")
        if not abstention_correct:
            print(f"    ⚠️  Abstention mismatch: expected={test_case['should_abstain']}, got={abstained}")
        if elements_missing:
            print(f"    ⚠️  Missing elements: {', '.join(elements_missing)}")
        if passed:
            print(f"    ✓ All checks passed in {result['resolution_time_seconds']}s")
        
        return test_result
    
    def run_all_tests(self):
        """Run all test cases and generate report"""
        print("=" * 70)
        print("🧪 AI AGENT QA TEST SUITE")
        print("=" * 70)
        
        test_cases = self.load_test_cases()
        
        for test_case in test_cases:
            result = self.run_test_case(test_case)
            self.results.append(result)
        
        # Generate summary
        self.print_summary()
        
        # Save results
        self.save_results()
        
        return self.results
    
    def print_summary(self):
        """Print test summary"""
        total = len(self.results)
        passed = sum(1 for r in self.results if r["passed"])
        failed = total - passed
        pass_rate = (passed / total * 100) if total > 0 else 0
        
        critical_tests = [r for r in self.results if r["priority"] == "critical"]
        critical_passed = sum(1 for r in critical_tests if r["passed"])
        critical_total = len(critical_tests)
        
        print("\n" + "=" * 70)
        print("📊 TEST SUMMARY")
        print("=" * 70)
        print(f"Total Tests: {total}")
        print(f"Passed: {passed} ✅")
        print(f"Failed: {failed} ❌")
        print(f"Pass Rate: {pass_rate:.1f}%")
        print(f"\nCritical Tests: {critical_passed}/{critical_total} passed")
        
        if failed > 0:
            print("\n⚠️  FAILED TESTS:")
            for result in self.results:
                if not result["passed"]:
                    print(f"  - {result['test_id']}: {result['description']}")
                    if not result["abstention_correct"]:
                        print(f"    Issue: Abstention behavior incorrect")
                    if result["elements_missing"]:
                        print(f"    Issue: Missing elements: {', '.join(result['elements_missing'])}")
        
        print("\n" + "=" * 70)
        
        # Determine overall status
        if pass_rate >= 95:
            print("✅ QA SUITE PASSED - Ready for deployment consideration")
        elif pass_rate >= 85:
            print("⚠️  QA SUITE MARGINAL - Review failures before deployment")
        else:
            print("❌ QA SUITE FAILED - Significant issues, do not deploy")
        print("=" * 70)
    
    def save_results(self):
        """Save test results to file"""
        output_file = Path(__file__).parent / f"qa_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        with open(output_file, 'w') as f:
            json.dump({
                "run_timestamp": datetime.now().isoformat(),
                "total_tests": len(self.results),
                "passed": sum(1 for r in self.results if r["passed"]),
                "failed": sum(1 for r in self.results if not r["passed"]),
                "pass_rate": sum(1 for r in self.results if r["passed"]) / len(self.results) * 100,
                "results": self.results
            }, f, indent=2)
        
        print(f"\n💾 Results saved to: {output_file}")


def main():
    """Main entry point"""
    test_cases_file = Path(__file__).parent / "test_cases.json"
    
    if not test_cases_file.exists():
        print(f"❌ Test cases file not found: {test_cases_file}")
        sys.exit(1)
    
    runner = QARunner(str(test_cases_file))
    runner.run_all_tests()


if __name__ == "__main__":
    main()
