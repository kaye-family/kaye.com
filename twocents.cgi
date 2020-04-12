#!/bin/perl
#
$cgidirectory="/cgi-bin";
$htmldirectory="/twocents";
$datadirectory="/web/htdocs/kaye/twocents";
&readparse;
print "Content-type: text/html\n\n";
#
#********* BEGIN BODY********************
  
#Update the LOGFILE:
#open (LOGFILE, ">>$datadirectory/chooser.log");
#$newline=join('::',@value); 
#print LOGFILE ("$newline\n"); 
#close LOGFILE; 

$posttwocents=$value[0];

#
#********* Do the main web page:
print "<html>\n";
print "<head>\n";
print "  <title>two cents</title>\n";
print "</head>\n";
print "<body bgcolor='#000000' vlink='#ff0000' alink='#ffffff' link='#ff0000'>\n";
print "<table width='100%' height='100%' border='0'><tr><td valign='middle' align='center'>\n";
print "\n";
print "<table width='420' rows='4' cols='1' border='0' cellspacing='0' cellpadding='10'>\n";
print "  <tr><td valign='bottom' align='center'>\n";
print "    <img width='400' height='60' alt='two cents' src='$htmldirectory/images/twocents.gif'>\n";
print "  </td></tr>\n";
print "  <tr><td valign='bottom' align='left'>\n";
print "    <p>\n";
print "      <p>1. </p>give your $.02<br>\n";
print "    </p>\n";
print "    <form action='$cgidirectory/twocents.cgi' method='post'>\n";
print "      <textarea name='input' cols='40' rows='10'></textarea><br>\n";
print "      <input type='submit' value='deposit'>\n";
print "    </form>\n";
print "  </td></tr>\n";
print "  <tr><td valign='bottom' align='left'>\n";
print "    <p>\n";
print "      <p>2. </p>get $.02 back<br><br>\n";
print "    </p>\n";
print "    <table width='400' border='0' cellspacing='0' cellpadding='0'><tr><td bgcolor='#ffffff' valign='middle' align='left'>\n";
print "      <p>\n";

#Deposit and Return Two Cents:
if ($posttwocents)
{
  open(LIST, "<$datadirectory/twocents.list");
  @tclist = <LIST>; 
  print LIST ("$posttwocents\n"); 
  close LIST;
  print "TWO CENTS!";
}

print "      </p>\n";
print "    </td></tr></table>\n";
print "  </td></tr>\n";
print "  <tr><td valign='bottom' align='left'>\n";
print "    <p>\n";
print "      the content of this site is completely uncensored<br><br>\n";
print "      your mind will be exposed at random to others' minds, and we take no responsibility for the consequences.\n";
print "    </p>\n";
print "  </td></tr>\n";
print "</table>\n";
print "\n";
print "</td></tr></table>\n";
print "</body>\n";
print "</html>\n";



#******** END BODY************************
#
# EACH VALUE IN THE HTML FORM WILL BE CONTAINED IN
# THE THE @VALUE ARRAY.
sub readparse {
read(STDIN,$user_string,$ENV{'CONTENT_LENGTH'});
if (length($ENV{'QUERY_STRING'})>0) {$user_string=$ENV{'QUERY_STRING'}};
$user_string =~ s/\+/ /g;
@name_value_pairs = split(/&/,$user_string);
foreach $name_value_pair (@name_value_pairs) {
        ($keyword,$value) = split(/=/,$name_value_pair);
        $value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C",hex($1))/ge;
        push(@value, "$value");
	  $user_data{$keyword} = $value;
	  if ($value=~/<!--\#exec/) {
		print "Content-type: text/html\n\nNo SSI permitted";
		exit;
	  };
};
};



#E-MAIL SUBROUTINE  
#ADD "&email(to,from,subject,text)" TO YOUR SCRIPT 
#REMEMBER TO BACKSLASH THE @ WHEN YOU ARE NOT USING IT IN AN ARRAY
#FOR EXAMPLE:
# $to='robyoung\@mediaone.net';  
# $from='foo\@company.com';
# $subject='Thank you for your inquiry';
# $text='Dear reader\n\nThank you for your recent inquiry.';
# &email($to,$from,$subject,$text);

sub email {
local($to,$from,$sub,$letter) = @_;
$to=~s/@/\@/;
$from=~s/@/\@/;
open(MAIL, "|/usr/lib/sendmail -t") || die
"Content-type: text/text\n\nCan't open /usr/lib/sendmail!";
print MAIL "To: $to\n";
print MAIL "From: $from\n";
print MAIL "Subject: $sub\n";
print MAIL "$letter\n";
return close(MAIL);
}
