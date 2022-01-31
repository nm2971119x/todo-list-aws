#!/usr/bin/perl

$ARGV[0] =~ /^(\d+).(\d+).(\d+)$/; 
my ($v,$j,$m) = ($1,$2,$3); $m++; 
print qq{$v.$j.$m};
