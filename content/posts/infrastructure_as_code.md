+++
author = "Sushant Srivastava"
date = "2014-12-01"
description = "Ansible is a good candidate for Infrasture as Code Solution."
draft = false
keywords = ["infrastructure","code","ansible","aws"]
tags = ["infrastructure","code","ansible","aws"]
title = "Infrastructure as Code"
topics = ["Infrastucture"]
type = "post"
+++

The book [Web
Operations](http://shop.oreilly.com/product/0636920000136.do) from
O'Reilly lists ten important principles for any configuration service.
It gives [Chef](https://www.getchef.com/chef/) as an example of an ideal
configuration management service because it fits all the general ten
principles. I argue that [Ansible](http://www.ansible.com/home) is also
a good option for a configuration service.

Modularity
==========

> Do one thing and do it well.

Ansible is a provisioning tool, that's it and it does its job well.

Cooperative
===========

> It takes a village.

You can call other services from Ansible. You can call your
infrastructure services like AWS from [aws ansible
module](http://docs.ansible.com/guide_aws.html). You can also configure
your DNS Services like
[DNSSimple](http://docs.ansible.com/dnsimple_module.html),
[Rackspace](http://docs.ansible.com/rax_dns_record_module.html),
[Route53](http://docs.ansible.com/route53_module.html) and [Digital
Ocean](http://docs.ansible.com/digital_ocean_domain_module.html) from
Ansible.

Composable
==========

> It should be ready for anything.

Ansible is configured using playbooks which are [YAML](http://yaml.org)
files. An Ansible role is actually a set of instructions to install and
configure any application. To install mysql and git on a server, you can
include roles for both mysql and git in your playbook.

Flexible
========

> It should be capable of doing whatever is required.

Ansible is written in [Python](http://python.org) Programming language
which is very flexible. You can also include bash scripts in Ansible.

Extensible
==========

> When something new is encountered, it's easy to extend.

You can write Ansible modules in any language of your choice, provided
you have an interpreter of that language. Ansible provides a
Python library for writing custom modules.

Repeatable
==========

> No matter how many times you do it, it works the same way.

Ansible Playbooks make your installations, upgrades, and day-to-day
management repeatable and reliable.

Declarative
===========

> It is about what you want, not how you do it.

Ansible is declarative with playbooks written in YAML syntax.

Abstract
========

> It takes care of the details for you.

Ansible provides a thin layer of abstraction. Some configuration
management tools provide a layer of abstraction over the specifics of
the different operating systems running on the remote servers, so that
you can use the same configuration management scripts to manage servers
running different operating systems. For example, instead of having to
deal with a specific package manager like yum or apt, the configuration
management tool exposes a “package” abstraction that you use instead.
Ansible isn’t like that. You have to use the “apt” module to install
packages on apt-based systems and the “yum” module to install packages
on yum-based systems. It isn't a disadvantage, in practice I found it to
be useful. Roles is a way of collecting playbooks together so they could
potentially be reused, as well as Ansible Galaxy, which is an online
repository of these roles.

Idempotent
==========

> It takes action only if it needs to.

Ansible [modules](http://docs.ansible.com/modules.html) are idempotent,
they will seek to avoid changes to system unless a change has to be
made.

Convergence
===========

> It takes care of itself and relies on other services to do the same.

Ansible modules are self aware and Ansible isn't any different from Chef
here.
