#!/usr/bin/env ruby

input = ARGV[0]

matches = input.scan(/School/)

if !matches.empty?
  puts matches.join
else
  puts ""
end
