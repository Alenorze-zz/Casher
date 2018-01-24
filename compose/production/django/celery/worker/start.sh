#!/usr/bin/env bash

set -o errexit
set -o pipefail
set -o nounset


celery -A src.taskapp worker -l INFO
