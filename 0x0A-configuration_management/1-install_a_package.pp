#!/usr/bin/env puppet
# Installs Flask from pip3

package { 'python3-pip':
  ensure  => installed,
}

exec {'install_flask':
  command => '/usr/bin/pip3 install flask==2.1.0',
  path    => ['/usr/bin', '/bin'],
  unless  => '/usr/bin/pip3 show flask | grep "Version: 2.1.0"',
  require => Package['python3-pip'],
}
