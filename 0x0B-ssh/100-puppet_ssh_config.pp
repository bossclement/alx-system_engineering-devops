# Puppet script to create an ssh config file
file_line { 'Turn off passwd auth':
  path => '/etc/ssh/sshd_config',
  line => 'PasswordAuthentication no',
}

file_line { 'Declare identity file':
  path => '/etc/ssh/ssh_config',
  line => 'IdentityFile ~/.ssh/school',
}

service { 'ssh':
  ensure => 'running',
}

