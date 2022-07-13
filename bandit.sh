#!/usr/bin/env bash
set -euf -o pipefail

pip install bandit

bandit -r $INPUT_PROJECT_PATH -o $GITHUB_WORKSPACE/output/security_report.txt -f 'txt'

if [ $? -eq 0 ]; then
    echo "🔥🔥🔥🔥Security check passed🔥🔥🔥🔥"
else
    echo "🔥🔥🔥🔥Security check failed🔥🔥🔥🔥"
    cat $GITHUB_WORKSPACE/output/security_report.txt
    exit 1
fi
