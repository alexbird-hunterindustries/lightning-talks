#!/usr/bin/env bash

function sauce {
  file_name="$1"
  child_processes="$2"

  directory="$(dirname "${file_name}")"
  npx nodemon@latest --exec "npx @marp-team/marp-cli@latest $file_name" --watch "$directory" --ext "*" --ignore "**/*.html" &
}
export -f sauce

find . -name "presentation.md" -exec bash -c "sauce {} $child_processes" \;

read
