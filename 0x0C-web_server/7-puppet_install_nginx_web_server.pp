# install NGINX usping puppet

class webserver {
    package { 'nginx':
        ensure => 'installed',
    }

    file { '/var/www/html/index.html':
        content => 'Hello World!',
    }

    service { 'nginx':
        ensure => 'running',
        enable => true,
    }

    file { '/etc/nginx/sites-available/default':
        ensure  => 'absent',
        require => Package['nginx'],
    }

    file { '/etc/nginx/sites-available/redirect_me':
        content => "
server {
    listen 80;
    server_name _;

    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }

    location / {
        root /var/www/html;
        index index.html;
    }
}",
        require => Package['nginx'],
    }

    file { '/etc/nginx/sites-enabled/redirect_me':
        ensure  => 'link',
        target  => '/etc/nginx/sites-available/redirect_me',
        require => File['/etc/nginx/sites-available/redirect_me'],
    }

    file { '/etc/nginx/sites-enabled/default':
        ensure  => 'absent',
        require => Package['nginx'],
    }

    exec { 'nginx_reload':
        command => 'service nginx reload',
        require => [Package['nginx'], File['/etc/nginx/sites-enabled/redirect_me']],
    }
}

class { 'webserver': }

