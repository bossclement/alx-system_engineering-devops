#!/usr/bin/env ruby

input = ARGV[0]

match = /School/.match(input)

if match
  puts "School"
else
  puts ""
end
