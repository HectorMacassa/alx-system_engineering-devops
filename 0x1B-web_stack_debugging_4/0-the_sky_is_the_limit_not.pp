# Ensure the ULIMIT is increased for Nginx
exec { 'fix--for-nginx':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => ['/usr/local/bin', '/bin', '/usr/bin'],
  onlyif  => 'grep -q "ulimit -n 15" /etc/default/nginx',
  notify  => Exec['nginx-restart'],
}

# Restart Nginx service to apply changes
exec { 'nginx-restart':
  command     => '/etc/init.d/nginx restart',
  path        => ['/usr/local/bin', '/bin', '/usr/bin', '/sbin'],
  refreshonly => true,
}
