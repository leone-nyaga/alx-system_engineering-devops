#!/usr/bin/pup
# Install an especific version of flask (2.1.0)

package { 'python3-pip':
  ensure => present,
}

exec { 'install_flask':
  command     => '/usr/bin/pip3 install Flask==2.1.0',
  path        => '/usr/local/bin:/usr/bin:/bin',
  creates     => '/usr/local/bin/flask',
}
