#!/usr/bin/env bash
set -uf -o pipefail

pip install bandit
mkdir -p $GITHUB_WORKSPACE/output
touch $GITHUB_WORKSPACE/output/security_report.txt
bandit -ll -r $GITHUB_WORKSPACE -o $GITHUB_WORKSPACE/output/security_report.txt -f 'txt' --exclude **/tests/**

if [ $? -eq 0 ]; then
    echo "🔥🔥🔥🔥Security check passed🔥🔥🔥🔥"
else
    echo "🔥🔥🔥🔥Security check failed🔥🔥🔥🔥"
    cat $GITHUB_WORKSPACE/output/security_report.txt
    exit 1
fi
