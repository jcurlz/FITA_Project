import os
import sys
from behave.__main__ import main as behave_main

if __name__ == "__main__":
    features_path = os.path.join(os.getcwd(), "features")
    print(features_path)
    tags = sys.argv[1:] if len(sys.argv) > 1 else ['-t', 'widget']

    report_path = os.environ.get("REPORT_PATH", "reports/behave_report.html")
    os.makedirs(os.path.dirname(report_path), exist_ok=True)

    behave_args = [
        features_path,
        *tags,
        '--format', 'behave_html_formatter:HTMLFormatter',
        '--out', report_path,
        '--no-skipped',
        '--no-capture',
        '-f', 'plain'
    ]

    # Execute Behave
    exit_code = behave_main(behave_args)

    # You can add custom logic here based on the exit_code
    if exit_code != 0:
        print("Behave tests failed!")
    else:
        print("Behave tests passed successfully.")