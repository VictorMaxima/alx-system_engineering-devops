#!/usr/bin/env ruby

# Check if there is an argument provided
if ARGV.empty?
  puts "Usage: #{$0} <string>"
  exit 1
end

# Get the first command line argument
input_string = ARGV[0]

# Check if the input string matches the pattern
if input_string.match?(/[A-Z]/)
  puts input_string.scan(/[A-Z]/).join
else
  puts "No match"
end
