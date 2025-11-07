#!/usr/bin/env bash

function sauce {
  file_name="$1"
  child_processes="$2"

  directory="$(dirname "${file_name}")"
  marp_command="npx @marp-team/marp-cli@latest $file_name"
  npx nodemon@latest --on-change-only --exec "$marp_command" --watch "$directory" --ext "*" --ignore "**/*.html" &
}
export -f sauce

find . -name "presentation.md" -exec bash -c "sauce {} $child_processes" \;

read
