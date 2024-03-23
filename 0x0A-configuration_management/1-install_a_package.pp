# install_flask.pp

# Ensure python3-pip package is installed
package { 'python3-pip':
  ensure => installed,
}

# Execute pip3 command to install Flask version 2.1.0
exec { 'install_flask':
  command     => '/usr/bin/pip3 install Flask==2.1.0',
  path        => ['/usr/local/bin', '/usr/bin', '/bin'],
  unless      => '/usr/bin/pip3 show Flask | grep -q "Version: 2.1.0"',
  require     => Package['python3-pip'],
}
