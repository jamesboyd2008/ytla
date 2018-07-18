#!/usr/bin/perl -w
#
use strict;
use warnings;
use MongoDB ();
use Data::Dumper qw(Dumper);
 
my $client = MongoDB->connect();
my $db   = $client->get_database( 'ytla');
 
my $datavalues = $db->get_collection('datum');
 
my $all_datavalues = $datavalues->find;
#my $lo_freq = $datavalues->find({'lo_freq' => {'$lt' => 10000}});
#print $lo_freq;
while (my $doc = $all_datavalues->next) {
  print $doc->{'lo_freq'}."\n";
  print $doc->{'timestamp'}."\n";
    }
 
$db->drop;

