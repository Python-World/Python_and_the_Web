#!/usr/bin/expect

set msg "[lindex $argv 0]"
set sub "[lindex $argv 1]"
set creds "[lindex $argv 2]"
set target "[lindex $argv 3]"
set email "[lindex $argv 4]"

set timeout 10
spawn openssl s_client -connect smtp.gmail.com:465 -crlf -ign_eof

expect "220" {
send "EHLO localhost\n"

expect "250" {
send "AUTH PLAIN $creds\n"

expect "235" {
send "MAIL FROM: <$email>\n"

expect "250" {
send "RCPT TO: <$target>\n"

expect "250" {
send "DATA\n"

expect "354" {
send "Subject: $sub\n\n"
send "$msg \n"
send "\n.\n"

expect "250" {
send "quit\n"
            }
          }
        }
      }
    }
  }
}
