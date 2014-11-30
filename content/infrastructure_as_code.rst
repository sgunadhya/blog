Infrastructure as Code
#######################

:date: 1 December 2014
:tags: infrastructure,code,ansible,aws
:category: devops
:slug: infrastructure-as-code
:author: Sushant Srivastava
:summary: Ansible is a good candidate for Infrasture as Code Solution.

The book `Web Operations`_ from O'Reilly lists ten important principles for any configuration service.
It gives `Chef`_ as an example of an ideal configurations service because it fits all the general ten principles.
I argue that `Ansible`_ is also a good option for a configuration service.

Modularity
==========
Ansible is a modular tool. You can extend Ansible through its many `modules`_.

Cooperative
===========
You can call other services from Ansible. You can call your infrastructure services 
like AWS from `aws ansible module`_. You can also configure your DNS Services like `DNSSimple`_,
`Rackspace`_, `Route53`_ and `Digital Ocean`_ from Ansible.

Composable
==========

  It should be ready for anything.

Ansible is configured using playbooks which are `YAML`_ files. An Ansible role is actually a set of 
instructions to install and configure any application. To install mysql and git on a server, you can include
roles for both mysql and git in your playbook.

Flexible
========

  It should be capable of doing whatever is required.

Ansible is written in `Python`_ Programming language which is very flexible. You can 
also include bash scripts in Ansible.

Extensible
==========

  When something new is encountered, it's easy to extend.

You can write Ansible modules in any language of your choice, provided you have an
interpreter of that language. Ansible provides a `Python library` for writing custom modules.






.. _`Web Operations`: http://shop.oreilly.com/product/0636920000136.do
.. _`Chef`: https://www.getchef.com/chef/
.. _`Ansible`: http://www.ansible.com/home
.. _`modules`: http://docs.ansible.com/modules.html
.. _`aws ansible module`: http://docs.ansible.com/guide_aws.html
.. _`DNSSimple`: http://docs.ansible.com/dnsimple_module.html
.. _`Rackspace`: http://docs.ansible.com/rax_dns_record_module.html
.. _`Route53`: http://docs.ansible.com/route53_module.html
.. _`Digital Ocean`: http://docs.ansible.com/digital_ocean_domain_module.html
.. _`YAML`: http://yaml.org
.. _`Python`: http://python.org
.. _`Python library`: http://docs.ansible.com/developing_api.html
