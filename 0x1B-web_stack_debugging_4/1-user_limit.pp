# script
exec { 'increase_ulimit':
  command => '/bin/echo "holberton soft nofile 65535" | sudo tee -a /etc/security/limits.conf && /bin/echo "holberton hard nofile 65535" | sudo tee -a /etc/security/limits.conf',
  path    => ['/bin', '/usr/bin'],
}