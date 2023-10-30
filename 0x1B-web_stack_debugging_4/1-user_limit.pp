# script
class { 'limits':
  limits => {
    'holberton' => {
      'domain' => 'hard',
      'type'   => '-',
      'item'   => 'nofile',
      'value'  => '65535',
    },
    'holberton' => {
      'domain' => 'soft',
      'type'   => '-',
      'item'   => 'nofile',
      'value'  => '65535',
    },
  },
}
