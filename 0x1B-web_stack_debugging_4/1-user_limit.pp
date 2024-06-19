# Increase hard file limit for Holberton user.
exec { 'increase-hard-file-limit-for-holberton-user':
  command => 'sed -i "/^holberton.*hard.*nofile/s/[0-9]\+/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/:/usr/bin/',
}

# Increase soft file limit for Holberton user.
exec { 'increase-soft-file-limit-for-holberton-user':
  command => 'sed -i "/^holberton.*soft.*nofile/s/[0-9]\+/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/:/usr/bin/',
}

