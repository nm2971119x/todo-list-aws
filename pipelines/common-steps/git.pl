#!/usr/bin/perl

$ARGV[0] =~ /^(\d+).(\d+).(\d+)$/; 
my ($v,$j,$m) = ($1,$2,$3); $m++; 
my $version   = qq{$v.$j.$m};
qx{git tag -a $version -m"‘version $version"};
qx{git push origin --tags};
