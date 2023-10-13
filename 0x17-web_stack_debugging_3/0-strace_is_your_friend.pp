# A puppet script to replace a line in a file

$file_name = '/var/www/html/wp-settings.php'

exec { 'replace_line':
  command => "sed -i 's/phpp/php/g' ${file_name}",
  path    => ['/bin','/usr/bin']
}
