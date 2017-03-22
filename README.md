# openstack-conf-diff
diff tool for openstack config    
(config 보다가 하도 빼먹는 일이 많아서 config 항목 기준으로 정확하게 비교하기 위한 툴을 만듬)

## build
```
docker build  --build-arg PROJECT=keystone --build-arg OLDBRANCH=stable/newton --build-arg NEWBRANCH=stable/ocata -t test .
```

## run
```
docker run -ti test-al bash -c 'python ./diff.py /oldapp/etc/keystone.conf.sample /newapp/etc/keystone.conf.sample'
```

## 결과 보충 설명
개인적으로 아무래도 여기서 대부분 가장 중요한건 `appended section`, `appended item`, `changed default value` 일듯 함
```
아래 6개의 항목으로 구성됨 각각
----Deleted sections:----
-> 말그대로 없어진 section 에 대한 것들

----Deleted items:----
-> 말그대로 없어진 item 들에 대한 것들

----Appended sections:----
-> 말그대로 추가된 section 들에 대한 것들

----Appended items:----
-> 말그대로 추가된 item 들에 대한 것들

----Changed default value:----
-> default 값이 변경된 것들 (comment도 포함될 수 있음)

----Changed comment:----
-> comment가 변경된 것들

```

## result

<a href="http://showterm.io/6fd6b5d3f8c0636cfa44a" target="_blank">실행 화면 보기</a>

```diff
----Deleted sections:----

[os_inherit]

# DEPRECATED: This allows domain-based role assignments to be inherited to
# projects owned by that domain, or from parent projects to child projects.
# (boolean value)
# This option is deprecated for removal since M.
# Its value may be silently ignored in the future.
# Reason: The option to disable the OS-INHERIT functionality has been
# deprecated in the Mitaka release and will be removed in the Ocata release.
# Starting in the Ocata release, OS-INHERIT functionality will always be
# enabled.
# enabled = true

-------------------------

----Deleted items:----

[DEFAULT]

# DEPRECATED: Set this to false if you want to enable the ability for user,
# group and project entities to be moved between domains by updating their
# `domain_id` attribute. Allowing such movement is not recommended if the scope
# of a domain admin is being restricted by use of an appropriate policy file
# (see `etc/policy.v3cloudsample.json` as an example). This feature is
# deprecated and will be removed in a future release, in favor of strictly
# immutable domain IDs. (boolean value)
# This option is deprecated for removal since M.
# Its value may be silently ignored in the future.
# Reason: The option to set domain_id_immutable to false has been deprecated in
# the M release and will be removed in the O release.
# domain_id_immutable = true

# Seconds to wait before a cast expires (TTL). The default value of -1
# specifies an infinite linger period. The value of 0 specifies no linger
# period. Pending messages shall be discarded immediately when the socket is
# closed. Only supported by impl_zmq. (integer value)
# Deprecated group/name - [DEFAULT]/rpc_cast_timeout
# rpc_cast_timeout = -1


[endpoint_policy]

# DEPRECATED: Enable endpoint-policy functionality, which allows policies to be
# associated with either specific endpoints, or endpoints of a given service
# type. (boolean value)
# This option is deprecated for removal since M.
# Its value may be silently ignored in the future.
# Reason: The option to enable the OS-ENDPOINT-POLICY API extension has been
# deprecated in the M release and will be removed in the O release. The OS-
# ENDPOINT-POLICY API extension will be enabled by default.
# enabled = true


[ldap]

# DEPRECATED: Delete subtrees using the subtree delete control. Only enable
# this option if your LDAP server supports subtree deletion. This option is
# only used for write operations. (boolean value)
# This option is deprecated for removal since M.
# Its value may be silently ignored in the future.
# Reason: Write support for the LDAP identity backend has been deprecated in
# the Mitaka release and will be removed in the Ocata release.
# allow_subtree_delete = false

# DEPRECATED: DN of the "dummy member" to use when `[ldap] use_dumb_member` is
# enabled. This option is only used for write operations. (string value)
# This option is deprecated for removal since M.
# Its value may be silently ignored in the future.
# Reason: Write support for the LDAP identity backend has been deprecated in
# the Mitaka release and will be removed in the Ocata release.
# dumb_member = cn=dumb,dc=nonexistent

# DEPRECATED: If enabled, keystone is allowed to create groups in the LDAP
# server. (boolean value)
# This option is deprecated for removal since M.
# Its value may be silently ignored in the future.
# Reason: Write support for the LDAP identity backend has been deprecated in
# the Mitaka release and will be removed in the Ocata release.
# group_allow_create = true

# DEPRECATED: If enabled, keystone is allowed to delete groups in the LDAP
# server. (boolean value)
# This option is deprecated for removal since M.
# Its value may be silently ignored in the future.
# Reason: Write support for the LDAP identity backend has been deprecated in
# the Mitaka release and will be removed in the Ocata release.
# group_allow_delete = true

# DEPRECATED: If enabled, keystone is allowed to update groups in the LDAP
# server. (boolean value)
# This option is deprecated for removal since M.
# Its value may be silently ignored in the future.
# Reason: Write support for the LDAP identity backend has been deprecated in
# the Mitaka release and will be removed in the Ocata release.
# group_allow_update = true

# DEPRECATED: If true, keystone will add a dummy member based on the `[ldap]
# dumb_member` option when creating new groups. This is required if the object
# class for groups requires the `member` attribute. This option is only used
# for write operations. (boolean value)
# This option is deprecated for removal since M.
# Its value may be silently ignored in the future.
# Reason: Write support for the LDAP identity backend has been deprecated in
# the Mitaka release and will be removed in the Ocata release.
# use_dumb_member = false

# DEPRECATED: If enabled, keystone is allowed to create users in the LDAP
# server. (boolean value)
# This option is deprecated for removal since M.
# Its value may be silently ignored in the future.
# Reason: Write support for the LDAP identity backend has been deprecated in
# the Mitaka release and will be removed in the Ocata release.
# user_allow_create = true

# DEPRECATED: If enabled, keystone is allowed to delete users in the LDAP
# server. (boolean value)
# This option is deprecated for removal since M.
# Its value may be silently ignored in the future.
# Reason: Write support for the LDAP identity backend has been deprecated in
# the Mitaka release and will be removed in the Ocata release.
# user_allow_delete = true

# DEPRECATED: If enabled, keystone is allowed to update users in the LDAP
# server. (boolean value)
# This option is deprecated for removal since M.
# Its value may be silently ignored in the future.
# Reason: Write support for the LDAP identity backend has been deprecated in
# the Mitaka release and will be removed in the Ocata release.
# user_allow_update = true


[oslo_messaging_zmq]

# Seconds to wait before a cast expires (TTL). The default value of -1
# specifies an infinite linger period. The value of 0 specifies no linger
# period. Pending messages shall be discarded immediately when the socket is
# closed. Only supported by impl_zmq. (integer value)
# Deprecated group/name - [DEFAULT]/rpc_cast_timeout
# rpc_cast_timeout = -1


[token]

# DEPRECATED: This controls the hash algorithm to use to uniquely identify PKI
# tokens without having to transmit the entire token to keystone (which may be
# several kilobytes). This can be set to any algorithm that hashlib supports.
# WARNING: Before changing this value, the `auth_token` middleware protecting
# all other services must be configured with the set of hash algorithms to
# expect from keystone (both your old and new value for this option), otherwise
# token revocation will not be processed correctly. (string value)
# Allowed values: md5, sha1, sha224, sha256, sha384, sha512
# This option is deprecated for removal since M.
# Its value may be silently ignored in the future.
# Reason: PKI token support has been deprecated in the M release and will be
# removed in the O release. Fernet or UUID tokens are recommended.
# hash_algorithm = md5

-------------------------

----Appended sections:----

[healthcheck]

# Show more detailed information as part of the response (boolean value)
# detailed = false

# DEPRECATED: The path to respond to healtcheck requests on. (string value)
# This option is deprecated for removal.
# Its value may be silently ignored in the future.
# path = /healthcheck

# Additional backends that can perform health checks and report that
# information back as part of a request. (list value)
# backends =

# Check the presence of a file to determine if an application is running on a
# port. Used by DisableByFileHealthcheck plugin. (string value)
# disable_by_file_path = <None>

# Check the presence of a file based on a port to determine if an application
# is running on a port. Expects a "port:path" list of strings. Used by
# DisableByFilesPortsHealthcheck plugin. (list value)
# disable_by_file_paths =


[oslo_messaging_kafka]

# The time-to-live in sec of idle connections in the pool (integer value)
# conn_pool_ttl = 1200

# DEPRECATED: Default Kafka broker Host (string value)
# This option is deprecated for removal.
# Its value may be silently ignored in the future.
# Reason: Replaced by [DEFAULT]/transport_url
# kafka_default_host = localhost

# Pool Size for Kafka Consumers (integer value)
# pool_size = 10

# Size of batch for the producer async send (integer value)
# producer_batch_size = 16384

# Default timeout(s) for Kafka consumers (integer value)
# kafka_consumer_timeout = 1.0

# The pool size limit for connections expiration policy (integer value)
# conn_pool_min_size = 2

# Upper bound on the delay for KafkaProducer batching in seconds (floating
# point value)
# producer_batch_timeout = 0.0

# DEPRECATED: Default Kafka broker Port (port value)
# Minimum value: 0
# Maximum value: 65535
# This option is deprecated for removal.
# Its value may be silently ignored in the future.
# Reason: Replaced by [DEFAULT]/transport_url
# kafka_default_port = 9092

# Max fetch bytes of Kafka consumer (integer value)
# kafka_max_fetch_bytes = 1048576

# Group id for Kafka consumer. Consumers in one group will coordinate message
# consumption (string value)
# consumer_group = oslo_messaging_consumer

-------------------------

----Appended items:----

[DEFAULT]

# Maximum number of logged messages per rate_limit_interval. (integer value)
# rate_limit_burst = 0

# Log level name used by rate limiting: CRITICAL, ERROR, INFO, WARNING, DEBUG
# or empty string. Logs with level greater or equal to rate_limit_except_level
# are not filtered. An empty string means that all levels are filtered. (string
# value)
# rate_limit_except_level = CRITICAL

# Interval, number of seconds, of log rate limiting. (integer value)
# rate_limit_interval = 0

# Number of seconds to wait for an ack from a cast/call. After each retry
# attempt this timeout is multiplied by some specified multiplier. (integer
# value)
# rpc_ack_timeout_base = 15

# Number to multiply base ack timeout by after each retry attempt. (integer
# value)
# rpc_ack_timeout_multiplier = 2

# Expiration timeout in seconds of a sent/received message after which it is
# not tracked anymore by a client/server. (integer value)
# rpc_message_ttl = 300

# Default number of message sending attempts in case of any problems occurred:
# positive value N means at most N retries, 0 means no retries, None or -1 (or
# any other negative values) mean to retry forever. This option is used only if
# acknowledgments are enabled. (integer value)
# rpc_retry_attempts = 3

# Maximum number of (green) threads to work concurrently. (integer value)
# rpc_thread_pool_size = 100

# Wait for message acknowledgements from receivers. This mechanism works only
# via proxy without PUB/SUB. (boolean value)
# rpc_use_acks = false

# List of publisher hosts SubConsumer can subscribe on. This option has higher
# priority then the default publishers list taken from the matchmaker. (list
# value)
# subscribe_on =

# This option makes direct connections dynamic or static. It makes sense only
# with use_router_proxy=False which means to use direct connections for direct
# message types (ignored otherwise). (boolean value)
# use_dynamic_connections = false

# How many additional connections to a host will be made for failover reasons.
# This option is actual only in dynamic connections mode. (integer value)
# zmq_failover_connections = 2

# Number of seconds to wait before all pending messages will be sent after
# closing a socket. The default value of -1 specifies an infinite linger
# period. The value of 0 specifies no linger period. Pending messages shall be
# discarded immediately when the socket is closed. Positive values specify an
# upper bound for the linger period. (integer value)
# Deprecated group/name - [DEFAULT]/rpc_cast_timeout
# zmq_linger = -1

# Enable/disable TCP keepalive (KA) mechanism. The default value of -1 (or any
# other negative value) means to skip any overrides and leave it to OS default;
# 0 and 1 (or any other positive value) mean to disable and enable the option
# respectively. (integer value)
# zmq_tcp_keepalive = -1

# The number of retransmissions to be carried out before declaring that remote
# end is not available. The default value of -1 (or any other negative value
# and 0) means to skip any overrides and leave it to OS default. (integer
# value)
# zmq_tcp_keepalive_cnt = -1

# The duration between two keepalive transmissions in idle condition. The unit
# is platform dependent, for example, seconds in Linux, milliseconds in Windows
# etc. The default value of -1 (or any other negative value and 0) means to
# skip any overrides and leave it to OS default. (integer value)
# zmq_tcp_keepalive_idle = -1

# The duration between two successive keepalive retransmissions, if
# acknowledgement to the previous keepalive transmission is not received. The
# unit is platform dependent, for example, seconds in Linux, milliseconds in
# Windows etc. The default value of -1 (or any other negative value and 0)
# means to skip any overrides and leave it to OS default. (integer value)
# zmq_tcp_keepalive_intvl = -1


[auth]

# Entry point for the mapped auth plugin module in the `keystone.auth.mapped`
# namespace. You do not need to set this unless you are overriding keystone's
# own `mapped` authentication plugin. (string value)
# mapped = <None>


[ldap]

# The connection timeout to use with the LDAP server. A value of `-1` means
# that connections will never timeout. (integer value)
# Minimum value: -1
# connection_timeout = -1

# If enabled, group queries will use Active Directory specific filters for
# nested groups. (boolean value)
# group_ad_nesting = false


[oslo_messaging_amqp]

# The maximum number of attempts to re-send a reply message which failed due to
# a recoverable error. (integer value)
# Minimum value: -1
# default_reply_retry = 0

# The duration to schedule a purge of idle sender links. Detach link after
# expiry. (integer value)
# Minimum value: 1
# default_sender_link_timeout = 600

# Send messages of this type pre-settled.
# Pre-settled messages will not receive acknowledgement
# from the peer. Note well: pre-settled messages may be
# silently discarded if the delivery fails.
# Permitted values:
# 'rpc-call' - send RPC Calls pre-settled
# 'rpc-reply'- send RPC Replies pre-settled
# 'rpc-cast' - Send RPC Casts pre-settled
# 'notify'   - Send Notifications pre-settled
#  (multi valued)
#pre_settled = rpc-cast
# pre_settled = rpc-reply


[oslo_messaging_rabbit]

# Default serialization mechanism for serializing/deserializing
# outgoing/incoming messages (string value)
# Allowed values: json, msgpack
# default_serializer_type = json


[oslo_messaging_zmq]

# Number of seconds to wait for an ack from a cast/call. After each retry
# attempt this timeout is multiplied by some specified multiplier. (integer
# value)
# rpc_ack_timeout_base = 15

# Number to multiply base ack timeout by after each retry attempt. (integer
# value)
# rpc_ack_timeout_multiplier = 2

# Expiration timeout in seconds of a sent/received message after which it is
# not tracked anymore by a client/server. (integer value)
# rpc_message_ttl = 300

# Default number of message sending attempts in case of any problems occurred:
# positive value N means at most N retries, 0 means no retries, None or -1 (or
# any other negative values) mean to retry forever. This option is used only if
# acknowledgments are enabled. (integer value)
# rpc_retry_attempts = 3

# Maximum number of (green) threads to work concurrently. (integer value)
# rpc_thread_pool_size = 100

# Wait for message acknowledgements from receivers. This mechanism works only
# via proxy without PUB/SUB. (boolean value)
# rpc_use_acks = false

# List of publisher hosts SubConsumer can subscribe on. This option has higher
# priority then the default publishers list taken from the matchmaker. (list
# value)
# subscribe_on =

# This option makes direct connections dynamic or static. It makes sense only
# with use_router_proxy=False which means to use direct connections for direct
# message types (ignored otherwise). (boolean value)
# use_dynamic_connections = false

# How many additional connections to a host will be made for failover reasons.
# This option is actual only in dynamic connections mode. (integer value)
# zmq_failover_connections = 2

# Number of seconds to wait before all pending messages will be sent after
# closing a socket. The default value of -1 specifies an infinite linger
# period. The value of 0 specifies no linger period. Pending messages shall be
# discarded immediately when the socket is closed. Positive values specify an
# upper bound for the linger period. (integer value)
# Deprecated group/name - [DEFAULT]/rpc_cast_timeout
# zmq_linger = -1

# Enable/disable TCP keepalive (KA) mechanism. The default value of -1 (or any
# other negative value) means to skip any overrides and leave it to OS default;
# 0 and 1 (or any other positive value) mean to disable and enable the option
# respectively. (integer value)
# zmq_tcp_keepalive = -1

# The number of retransmissions to be carried out before declaring that remote
# end is not available. The default value of -1 (or any other negative value
# and 0) means to skip any overrides and leave it to OS default. (integer
# value)
# zmq_tcp_keepalive_cnt = -1

# The duration between two keepalive transmissions in idle condition. The unit
# is platform dependent, for example, seconds in Linux, milliseconds in Windows
# etc. The default value of -1 (or any other negative value and 0) means to
# skip any overrides and leave it to OS default. (integer value)
# zmq_tcp_keepalive_idle = -1

# The duration between two successive keepalive retransmissions, if
# acknowledgement to the previous keepalive transmission is not received. The
# unit is platform dependent, for example, seconds in Linux, milliseconds in
# Windows etc. The default value of -1 (or any other negative value and 0)
# means to skip any overrides and leave it to OS default. (integer value)
# zmq_tcp_keepalive_intvl = -1


[profiler]

#
# Document type for notification indexing in elasticsearch.
#  (string value)
# es_doc_type = notification

#
# Elasticsearch splits large requests in batches. This parameter defines
# maximum size of each batch (for example: es_scroll_size=10000).
#  (integer value)
# es_scroll_size = 10000

#
# This parameter is a time value parameter (for example: es_scroll_time=2m),
# indicating for how long the nodes that participate in the search will
# maintain
# relevant resources in order to continue and support it.
#  (string value)
# es_scroll_time = 2m

#
# Redissentinel uses a service name to identify a master redis service.
# This parameter defines the name (for example:
# sentinal_service_name=mymaster).
#  (string value)
# sentinel_service_name = mymaster

#
# Redissentinel provides a timeout option on the connections.
# This parameter defines that timeout (for example: socket_timeout=0.1).
#  (floating point value)
# socket_timeout = 0.1


[security_compliance]

# Enabling this option requires users to change their password when the user is
# created, or upon administrative reset. Before accessing any services,
# affected users will have to change their password. To ignore this requirement
# for specific users, such as service users, set the `options` attribute
# `ignore_change_password_upon_first_use` to `True` for the desired user via
# the update user API. This feature is disabled by default. This feature is
# only applicable with the `sql` backend for the `[identity] driver`. (boolean
# value)
# change_password_upon_first_use = false


[token]

# This controls the number of seconds that a token can be retrieved for beyond
# the built-in expiry time. This allows long running operations to succeed.
# Defaults to two days. (integer value)
# allow_expired_window = 172800

-------------------------

----Changed default value:----
* max_token_size
  # Similar to `[DEFAULT] max_param_size`, but provides an exception for token
+ # values. With Fernet tokens, this can be set as low as 255. With UUID tokens,
+ # this should be set to 32). (integer value)
- # values. With PKI / PKIZ tokens, this needs to be set close to 8192 (any
- # higher, and other HTTP implementations may break), depending on the size of
- # your service catalog and other factors. With Fernet tokens, this can be set
- # as low as 255. With UUID tokens, this should be set to 32). (integer value)
- # max_token_size = 8192
?                    ---
+ # max_token_size = 255
?                     ++

* notification_format
  # Define the notification format for identity service events. A `basic`
  # notification only has information about the resource being operated on. A
  # `cadf` notification has the same information, as well as information about
  # the initiator of the event. The `cadf` option is entirely backwards
  # compatible with the `basic` option, but is fully CADF-compliant, and is
  # recommended for auditing use cases. (string value)
  # Allowed values: basic, cadf
- # notification_format = basic
?                         ^ ^^^
+ # notification_format = cadf
?                         ^ ^^

* notification_opt_out
- # If left undefined, keystone will emit notifications for all types of events.
- # You can reduce the number of notifications keystone emits by using this
?                                                                ^^ ^^^ ^^^
+ # You can reduce the number of notifications keystone emits by explicitly
?                                                                ^^^^ ^^ ^^
- # option to enumerate notification topics that should be suppressed. Values are
- # expected to be in the form `identity.<resource_type>.<operation>`. This field
+ # opting out. Keystone will not emit notifications that match the patterns
+ # expressed in this list. Values are expected to be in the form of
+ # `identity.<resource_type>.<operation>`. By default, all notifications related
+ # to authentication are automatically suppressed. This field can be set
- # can be set multiple times in order to opt-out of multiple notification
?  -----------
+ # multiple times in order to opt-out of multiple notification topics. For
?                                                              ++++++++++++
- # topics. For example: notification_opt_out=identity.user.create
+ # example, the following suppresses notifications describing user creation or
+ # successful authentication events: notification_opt_out=identity.user.create
  # notification_opt_out=identity.authenticate.success (multi valued)
- # notification_opt_out =
+ #notification_opt_out = identity.authenticate.success
+ #notification_opt_out = identity.authenticate.pending
+ # notification_opt_out = identity.authenticate.failed

* use_pub_sub
  # Use PUB/SUB pattern for fanout methods. PUB/SUB always uses proxy. (boolean
  # value)
  # Deprecated group/name - [DEFAULT]/use_pub_sub
- # use_pub_sub = true
?                 ^^^
+ # use_pub_sub = false
?                 ^^^^

* use_router_proxy
  # Use ROUTER remote proxy. (boolean value)
  # Deprecated group/name - [DEFAULT]/use_router_proxy
- # use_router_proxy = true
?                      ^^^
+ # use_router_proxy = false
?                      ^^^^

* use_stderr
  # Log output to standard error. This option is ignored if log_config_append is
  # set. (boolean value)
- # use_stderr = true
?                ^^^
+ # use_stderr = false
?                ^^^^

* zmq_immediate
  # This option configures round-robin mode in zmq socket. True means not keeping
  # a queue when server side disconnects. False means to keep queue and messages
  # even if server is disconnected, when the server appears we send all
  # accumulated messages to it. (boolean value)
- # zmq_immediate = false
?                   ^^^^
+ # zmq_immediate = true
?                   ^^^


[assignment]

* driver
  # Entry point for the assignment backend driver (where role assignments are
  # stored) in the `keystone.assignment` namespace. Only a SQL driver is supplied
- # by keystone itself. If an assignment driver is not specified, the identity
- # driver will choose the assignment driver based on the deprecated
- # `[identity]/driver` option (the behavior will be removed in the "O" release).
- # Unless you are writing proprietary drivers for keystone, you do not need to
?                                                           -------------------
+ # by keystone itself. Unless you are writing proprietary drivers for keystone,
?  ++++++++++++++++++++
- # set this option. (string value)
+ # you do not need to set this option. (string value)
?  +++++++++++++++++++
- # driver = <None>
+ # driver = sql


[auth]

* methods
- # Allowed authentication methods. (list value)
+ # Allowed authentication methods. Note: You should disable the `external` auth
+ # method if you are currently using federation. External auth and federation
+ # both use the REMOTE_USER variable. Since both the mapped and external plugin
+ # are being invoked to validate attributes in the request environment, it can
+ # cause conflicts. (list value)
- # methods = external,password,token,oauth1
+ # methods = external,password,token,oauth1,mapped
?                                           +++++++

* use_pub_sub
  # Use PUB/SUB pattern for fanout methods. PUB/SUB always uses proxy. (boolean
  # value)
  # Deprecated group/name - [DEFAULT]/use_pub_sub
- # use_pub_sub = true
?                 ^^^
+ # use_pub_sub = false
?                 ^^^^

* use_router_proxy
  # Use ROUTER remote proxy. (boolean value)
  # Deprecated group/name - [DEFAULT]/use_router_proxy
- # use_router_proxy = true
?                      ^^^
+ # use_router_proxy = false
?                      ^^^^

* zmq_immediate
  # This option configures round-robin mode in zmq socket. True means not keeping
  # a queue when server side disconnects. False means to keep queue and messages
  # even if server is disconnected, when the server appears we send all
  # accumulated messages to it. (boolean value)
- # zmq_immediate = false
?                   ^^^^
+ # zmq_immediate = true
?                   ^^^


[resource]

* driver
  # Entry point for the resource driver in the `keystone.resource` namespace.
- # Only a `sql` driver is supplied by keystone. If a resource driver is not
?                                                ^^  -  ^^^^^^^^  ^^^^ -- ^^
+ # Only a `sql` driver is supplied by keystone. Unless you are writing
?                                                ^^^^^^^^^^    ^^  ^  ^
- # specified, the assignment driver will choose the resource driver to maintain
- # backwards compatibility with older configuration files. (string value)
- # driver = <None>
+ # proprietary drivers for keystone, you do not need to set this option. (string
+ # value)
+ # driver = sql


[token]

* cache_on_issue
  # Enable storing issued token data to token validation cache so that first
- # token validation doesn't actually cause full validation cycle. (boolean
?                                                                  ^^  ---
+ # token validation doesn't actually cause full validation cycle. This option
?                                                                  ^^^^^ +++
+ # has no effect unless global caching and token caching are enabled. (boolean
  # value)
- # cache_on_issue = false
?                    ^^^^
+ # cache_on_issue = true
?                    ^^^

* provider
  # Entry point for the token provider in the `keystone.token.provider`
  # namespace. The token provider controls the token construction, validation,
- # and revocation operations. Keystone includes `fernet`, `pkiz`, `pki`, and
?                                                        ----------------
+ # and revocation operations. Keystone includes `fernet` and `uuid` token
?                                                            +++++++++++++
- # `uuid` token providers. `uuid` tokens must be persisted (using the backend
?  -------------
+ # providers. `uuid` tokens must be persisted (using the backend specified in
?                                                                +++++++++++++
- # specified in the `[token] driver` option), but do not require any extra
?  -------------
+ # the `[token] driver` option), but do not require any extra configuration or
?                                                             +++++++++++++++++
- # configuration or setup. `fernet` tokens do not need to be persisted at all,
?  -----------------
+ # setup. `fernet` tokens do not need to be persisted at all, but require that
?                                                             +++++++++++++++++
- # but require that you run `keystone-manage fernet_setup` (also see the
?  -----------------
+ # you run `keystone-manage fernet_setup` (also see the `keystone-manage
?                                                       +++++++++++++++++
+ # fernet_rotate` command). (string value)
+ # provider = fernet
- # `keystone-manage fernet_rotate` command). `pki` and `pkiz` tokens can be
- # validated offline, without making HTTP calls to keystone, but require that
- # certificates be installed and distributed to facilitate signing tokens and
- # later validating those signatures. (string value)
- # provider = uuid

-------------------------

----Changed comment:----

[DEFAULT]

* admin_endpoint
  # The base admin endpoint URL for Keystone that is advertised to clients (NOTE:
  # this does NOT affect how Keystone listens for connections). Defaults to the
  # base host URL of the request. For example, if keystone receives a request to
  # `http://server:35357/v3/users`, then this will option will be automatically
  # treated as `http://server:35357`. You should only need to set option if
  # either the value of the base URL contains a path that keystone does not
  # automatically infer (`/prefix/v3`), or if the endpoint should be found on a
- # different host. (string value)
?                    ^^  --
+ # different host. (uri value)
?                    ^
  # admin_endpoint = <None>

* public_endpoint
  # The base public endpoint URL for Keystone that is advertised to clients
  # (NOTE: this does NOT affect how Keystone listens for connections). Defaults
  # to the base host URL of the request. For example, if keystone receives a
  # request to `http://server:5000/v3/users`, then this will option will be
  # automatically treated as `http://server:5000`. You should only need to set
  # option if either the value of the base URL contains a path that keystone does
  # not automatically infer (`/prefix/v3`), or if the endpoint should be found on
- # a different host. (string value)
?                      ^^  --
+ # a different host. (uri value)
?                      ^
  # public_endpoint = <None>

* rpc_zmq_matchmaker
  # MatchMaker driver. (string value)
- # Allowed values: redis, dummy
+ # Allowed values: redis, sentinel, dummy
?                          ++++++++++
  # Deprecated group/name - [DEFAULT]/rpc_zmq_matchmaker
  # rpc_zmq_matchmaker = redis


[kvs]

* backends
- # Extra `dogpile.cache` backend modules to register with the `dogpile.cache`
?                                                             ----------------
+ # DEPRECATED: Extra `dogpile.cache` backend modules to register with the
?  ++++++++++++
- # library. It is not necessary to set this value unless you are providing a
?                                                                ------------
+ # `dogpile.cache` library. It is not necessary to set this value unless you are
?  ++++++++++++++++
- # custom KVS backend beyond what `dogpile.cache` already supports. (list value)
?                                                                   -------------
+ # providing a custom KVS backend beyond what `dogpile.cache` already supports.
?  ++++++++++++
+ # (list value)
+ # This option is deprecated for removal since O.
+ # Its value may be silently ignored in the future.
+ # Reason: This option has been deprecated in the O release and will be removed
+ # in the P release. Use SQL backends instead.
  # backends =

* config_prefix
- # Prefix for building the configuration dictionary for the KVS region. This
?                                                               -------------
+ # DEPRECATED: Prefix for building the configuration dictionary for the KVS
?  ++++++++++++
- # should not need to be changed unless there is another `dogpile.cache` region
?                                                        -----------------------
+ # region. This should not need to be changed unless there is another
?  +++++++++++++
- # with the same configuration name. (string value)
+ # `dogpile.cache` region with the same configuration name. (string value)
?  +++++++++++++++++++++++
+ # This option is deprecated for removal since O.
+ # Its value may be silently ignored in the future.
+ # Reason: This option has been deprecated in the O release and will be removed
+ # in the P release. Use SQL backends instead.
  # config_prefix = keystone.kvs

* default_lock_timeout
- # Number of seconds after acquiring a distributed lock that the backend should
?                                                                ---------------
+ # DEPRECATED: Number of seconds after acquiring a distributed lock that the
?  ++++++++++++
- # consider the lock to be expired. This option should be tuned relative to the
?                                                               ----------------
+ # backend should consider the lock to be expired. This option should be tuned
?  +++++++++++++++
- # longest amount of time that it takes to perform a successful operation. If
?                                                               --------------
+ # relative to the longest amount of time that it takes to perform a successful
?  ++++++++++++++++
- # this value is set too low, then a cluster will end up performing work
?                                                        ----------------
+ # operation. If this value is set too low, then a cluster will end up
?  ++++++++++++++
- # redundantly. If this value is set too high, then a cluster will not be able
?                                                             -----------------
+ # performing work redundantly. If this value is set too high, then a cluster
?  ++++++++++++++++
- # to efficiently recover and retry after a failed operation. A non-zero value
?                                                               ---------------
+ # will not be able to efficiently recover and retry after a failed operation. A
?  +++++++++++++++++
- # is recommended if the backend supports lock timeouts, as zero prevents locks
?                                                                ---------------
+ # non-zero value is recommended if the backend supports lock timeouts, as zero
?  +++++++++++++++
- # from expiring altogether. (integer value)
+ # prevents locks from expiring altogether. (integer value)
?  +++++++++++++++
  # Minimum value: 0
+ # This option is deprecated for removal since O.
+ # Its value may be silently ignored in the future.
+ # Reason: This option has been deprecated in the O release and will be removed
+ # in the P release. Use SQL backends instead.
  # default_lock_timeout = 5

* enable_key_mangler
- # Set to false to disable using a key-mangling function, which ensures fixed-
?                                                               ---------------
+ # DEPRECATED: Set to false to disable using a key-mangling function, which
?  ++++++++++++
- # length keys are used in the KVS store. This is configurable for debugging
?                                                                  ----------
+ # ensures fixed-length keys are used in the KVS store. This is configurable for
?   ++++++++++++++
- # purposes, and it is therefore highly recommended to always leave this set to
?                                                                   ------------
+ # debugging purposes, and it is therefore highly recommended to always leave
?  ++++++++++
- # true. (boolean value)
+ # this set to true. (boolean value)
?  ++++++++++++
+ # This option is deprecated for removal since O.
+ # Its value may be silently ignored in the future.
+ # Reason: This option has been deprecated in the O release and will be removed
+ # in the P release. Use SQL backends instead.
  # enable_key_mangler = true


[ldap]

* group_attribute_ignore
- # DEPRECATED: List of group attributes to ignore on create and update. This is
?  ------------                                                          ^ ^^^^^
+ # List of group attributes to ignore on create and update. or whether a
?                                                            ^^^^ ^^^^^^^
+ # specific group attribute should be filtered for list or show group. (list
+ # value)
- # only used for write operations. (list value)
- # This option is deprecated for removal since M.
- # Its value may be silently ignored in the future.
- # Reason: Write support for the LDAP identity backend has been deprecated in
- # the Mitaka release and will be removed in the Ocata release.
  # group_attribute_ignore =

* pool_connection_timeout
- # The connection timeout to use with the LDAP server. A value of `-1` means
?                                  -----         -----                 ------
+ # The connection timeout to use when pooling LDAP connections. A value of `-1`
?                                    +++++++++      ++++++++++
- # that connections will never timeout. This option has no effect unless `[ldap]
?                                                                        --------
+ # means that connections will never timeout. This option has no effect unless
?  ++++++
- # use_pool` is also enabled. (integer value)
+ # `[ldap] use_pool` is also enabled. (integer value)
?  ++++++++
  # Minimum value: -1
  # pool_connection_timeout = -1

* user_attribute_ignore
- # DEPRECATED: List of user attributes to ignore on create and update. This is
?  ------------                                                       ^^^  ^^ ^
+ # List of user attributes to ignore on create and update, or whether a specific
?                                                         ^^^^^^ ++++++++++++ ^ ^
+ # user attribute should be filtered for list or show user. (list value)
- # only used for write operations. (list value)
- # This option is deprecated for removal since M.
- # Its value may be silently ignored in the future.
- # Reason: Write support for the LDAP identity backend has been deprecated in
- # the Mitaka release and will be removed in the Ocata release.
  # user_attribute_ignore = default_project_id


[matchmaker_redis]

* sentinel_hosts
- # DEPRECATED: List of Redis Sentinel hosts (fault tolerance mode) e.g.
+ # DEPRECATED: List of Redis Sentinel hosts (fault tolerance mode), e.g.,
?                                                                  +     +
  # [host:port, host1:port ... ] (list value)
  # This option is deprecated for removal.
  # Its value may be silently ignored in the future.
  # Reason: Replaced by [DEFAULT]/transport_url
  # sentinel_hosts =

* socket_timeout
- # Timeout in ms on blocking socket operations (integer value)
+ # Timeout in ms on blocking socket operations. (integer value)
?                                              +
  # socket_timeout = 10000


[memcache]

* dead_retry
  # Number of seconds memcached server is considered dead before it is tried
- # again. This is used by the key value store system (including, the `memcache`
?                                                        ^  -------- ^^^^^^^^^^^
+ # again. This is used by the key value store system. (integer value)
?                                                    +    ^^^^^^^^   ^
- # and `memcache_pool` options for the `[token] driver` persistence backend).
- # (integer value)
  # dead_retry = 300

* pool_connection_get_timeout
  # Number of seconds that an operation will wait to get a memcache client
- # connection. This is used by the key value store system (including, the
?                                                             ^  --------
+ # connection. This is used by the key value store system. (integer value)
?                                                         +    ^^^^^^^^   +
- # `memcache` and `memcache_pool` options for the `[token] driver` persistence
- # backend). (integer value)
  # pool_connection_get_timeout = 10

* pool_maxsize
  # Max total number of open connections to every memcached server. This is used
+ # by the key value store system. (integer value)
- # by the key value store system (including, the `memcache` and `memcache_pool`
- # options for the `[token] driver` persistence backend). (integer value)
  # pool_maxsize = 10

* pool_unused_timeout
  # Number of seconds a connection to memcached is held unused in the pool before
- # it is closed. This is used by the key value store system (including, the
?                                                               ^  --------
+ # it is closed. This is used by the key value store system. (integer value)
?                                                           +    ^^^^^^^^   +
- # `memcache` and `memcache_pool` options for the `[token] driver` persistence
- # backend). (integer value)
  # pool_unused_timeout = 60

* servers
- # Comma-separated list of memcached servers in the format of
+ # DEPRECATED: Comma-separated list of memcached servers in the format of
?  ++++++++++++
  # `host:port,host:port` that keystone should use for the `memcache` token
  # persistence provider and other memcache-backed KVS drivers. This
  # configuration value is NOT used for intermediary caching between keystone and
  # other backends, such as SQL and LDAP (for that, see the `[cache]` section).
  # Multiple keystone servers in the same deployment should use the same set of
  # memcached servers to ensure that data (such as UUID tokens) created by one
  # node is available to the others. (list value)
+ # This option is deprecated for removal since O.
+ # Its value may be silently ignored in the future.
+ # Reason: This option has been deprecated in the O release and will be removed
+ # in the P release. Use oslo.cache instead.
  # servers = localhost:11211

* socket_timeout
  # Timeout in seconds for every call to a server. This is used by the key value
+ # store system. (integer value)
- # store system (including, the `memcache` and `memcache_pool` options for the
- # `[token] driver` persistence backend). (integer value)
  # socket_timeout = 3


[oslo_messaging_amqp]

* allow_insecure_clients
- # Accept clients using either SSL or plain TCP (boolean value)
+ # DEPRECATED: Accept clients using either SSL or plain TCP (boolean value)
?  ++++++++++++
  # Deprecated group/name - [amqp1]/allow_insecure_clients
+ # This option is deprecated for removal.
+ # Its value may be silently ignored in the future.
+ # Reason: Not applicable - not a SSL server
  # allow_insecure_clients = false

* default_reply_timeout
- # The deadline for an rpc reply message delivery. Only used when caller does
?                                                   ^ ^^^^^ ^^^^ ^^^  ^ ^^^^^^
+ # The deadline for an rpc reply message delivery. (integer value)
?                                                   ^^ ^ ^ ^^^  ^ ^
- # not provide a timeout expiry. (integer value)
  # Minimum value: 5
  # default_reply_timeout = 30

* ssl_ca_file
- # CA certificate PEM file to verify server certificate (string value)
?                                                               -------
+ # CA certificate PEM file used to verify the server's certificate (string
?                           +++++          ++++      ++
+ # value)
  # Deprecated group/name - [amqp1]/ssl_ca_file
  # ssl_ca_file =

* ssl_cert_file
- # Identifying certificate PEM file to present to clients (string value)
+ # Self-identifying certificate PEM file for client authentication (string
+ # value)
  # Deprecated group/name - [amqp1]/ssl_cert_file
  # ssl_cert_file =

* ssl_key_file
- # Private key PEM file used to sign cert_file certificate (string value)
?                                                            ^ -  ---  --
+ # Private key PEM file used to sign ssl_cert_file certificate (optional)
?                                     ++++                       ^^  +
+ # (string value)
  # Deprecated group/name - [amqp1]/ssl_key_file
  # ssl_key_file =


[oslo_messaging_rabbit]

* default_rpc_retry_attempts
  # Reconnecting retry count in case of connectivity problem during sending RPC
  # message, -1 means infinite retry. If actual retry attempts in not 0 the rpc
- # request could be processed more then one time (integer value)
?                                     ^
+ # request could be processed more than one time (integer value)
?                                     ^
  # default_rpc_retry_attempts = -1

* rabbit_ha_queues
  # Try to use HA queues in RabbitMQ (x-ha-policy: all). If you change this
  # option, you must wipe the RabbitMQ database. In RabbitMQ 3.0, queue mirroring
  # is no longer controlled by the x-ha-policy argument when declaring a queue.
- # If you just want to make sure that all queues (except  those with auto-
?                                                         -
+ # If you just want to make sure that all queues (except those with auto-
  # generated names) are mirrored across all nodes, run: "rabbitmqctl set_policy
  # HA '^(?!amq\.).*' '{"ha-mode": "all"}' " (boolean value)
  # Deprecated group/name - [DEFAULT]/rabbit_ha_queues
  # rabbit_ha_queues = false

* rabbit_login_method
  # The RabbitMQ login method. (string value)
+ # Allowed values: PLAIN, AMQPLAIN, RABBIT-CR-DEMO
  # Deprecated group/name - [DEFAULT]/rabbit_login_method
  # rabbit_login_method = AMQPLAIN


[oslo_messaging_zmq]

* rpc_zmq_matchmaker
  # MatchMaker driver. (string value)
- # Allowed values: redis, dummy
+ # Allowed values: redis, sentinel, dummy
?                          ++++++++++
  # Deprecated group/name - [DEFAULT]/rpc_zmq_matchmaker
  # rpc_zmq_matchmaker = redis


[oslo_policy]

* policy_file
- # The JSON file that defines policies. (string value)
?      -----
+ # The file that defines policies. (string value)
  # Deprecated group/name - [DEFAULT]/policy_file
  # policy_file = policy.json


[profiler]

* connection_string
  #
  # Connection string for a notifier backend. Default value is messaging:// which
  # sets the notifier to oslo_messaging.
  #
  # Examples of possible values:
  #
  # * messaging://: use oslo_messaging driver for sending notifications.
+ # * mongodb://127.0.0.1:27017 : use mongodb driver for sending notifications.
+ # * elasticsearch://127.0.0.1:9200 : use elasticsearch driver for sending
+ # notifications.
  #  (string value)
  # connection_string = messaging://


[security_compliance]

* password_expires_ignore_user_ids
- # Comma separated list of user IDs to be ignored when checking if a password is
?                                                                    ------------
+ # DEPRECATED: Comma separated list of user IDs to be ignored when checking if a
?  ++++++++++++
- # expired. Passwords for users in this list will not expire. This feature will
?                                                                  -------------
+ # password is expired. Passwords for users in this list will not expire. This
?  ++++++++++++
- # only be enabled if `[security_compliance] password_expires_days` is set.
?                                                                   --------
+ # feature will only be enabled if `[security_compliance] password_expires_days`
?  +++++++++++++
- # (list value)
+ # is set. (list value)
?  ++++++++
+ # This option is deprecated for removal since O.
+ # Its value may be silently ignored in the future.
+ # Reason: Functionality added as a per-user option "ignore_password_expiry" in
+ # Ocata. Each user that should ignore password expiry should have the value set
+ # to "true" in the user's `options` attribute (e.g.
+ # `user['options']['ignore_password_expiry'] = True`) with an "update_user"
+ # call. This avoids the need to restart keystone to adjust the users that
+ # ignore password expiry. This option will be removed in the Pike release.
  # password_expires_ignore_user_ids =


[signing]

* ca_certs
- # DEPRECATED: Absolute path to the public certificate authority (CA) file to
?  ------------
+ # Absolute path to the public certificate authority (CA) file to use when
?                                                                 +++++++++
- # use when creating self-signed certificates with `keystone-manage pki_setup`.
?  ---------
+ # creating self-signed certificates with `keystone-manage pki_setup`. Set this
?                                                                      +++++++++
- # Set this together with `[signing] ca_key`. There is no reason to set this
?  ---------
+ # together with `[signing] ca_key`. There is no reason to set this option
?                                                                   +++++++
+ # unless you are requesting revocation lists in a non-production environment.
+ # Use a `[signing] certfile` issued from a trusted certificate authority
+ # instead. (string value)
- # option unless you are using a `pki` or `pkiz` `[token] provider` value in a
- # non-production environment. Use a `[signing] certfile` issued from a trusted
- # certificate authority instead. (string value)
- # This option is deprecated for removal since M.
- # Its value may be silently ignored in the future.
- # Reason: PKI token support has been deprecated in the M release and will be
- # removed in the O release. Fernet or UUID tokens are recommended.
  # ca_certs = /etc/keystone/ssl/certs/ca.pem

* ca_key
- # DEPRECATED: Absolute path to the private certificate authority (CA) key file
?  ------------
+ # Absolute path to the private certificate authority (CA) key file to use when
?                                                                   ++++++++++++
- # to use when creating self-signed certificates with `keystone-manage
?  ------------
+ # creating self-signed certificates with `keystone-manage pki_setup`. Set this
?                                                          +++++++++++++++++++++
+ # together with `[signing] ca_certs`. There is no reason to set this option
+ # unless you are requesting revocation lists in a non-production environment.
+ # Use a `[signing] certfile` issued from a trusted certificate authority
+ # instead. (string value)
- # pki_setup`. Set this together with `[signing] ca_certs`. There is no reason
- # to set this option unless you are using a `pki` or `pkiz` `[token] provider`
- # value in a non-production environment. Use a `[signing] certfile` issued from
- # a trusted certificate authority instead. (string value)
- # This option is deprecated for removal since M.
- # Its value may be silently ignored in the future.
- # Reason: PKI token support has been deprecated in the M release and will be
- # removed in the O release. Fernet or UUID tokens are recommended.
  # ca_key = /etc/keystone/ssl/private/cakey.pem

* cert_subject
- # DEPRECATED: The certificate subject to use when generating a self-signed
?  ------------
+ # The certificate subject to use when generating a self-signed token signing
?                                                               ++++++++++++++
- # token signing certificate. There is no reason to set this option unless you
?  --------------
+ # certificate. There is no reason to set this option unless you are requesting
?                                                                +++++++++++++++
+ # revocation lists in a non-production environment. Use a `[signing] certfile`
+ # issued from a trusted certificate authority instead. (string value)
- # are using a `pki` or `pkiz` `[token] provider` value in a non-production
- # environment. Use a `[signing] certfile` issued from a trusted certificate
- # authority instead. (string value)
- # This option is deprecated for removal since M.
- # Its value may be silently ignored in the future.
- # Reason: PKI token support has been deprecated in the M release and will be
- # removed in the O release. Fernet or UUID tokens are recommended.
  # cert_subject = /C=US/ST=Unset/L=Unset/O=Unset/CN=www.example.com

* certfile
- # DEPRECATED: Absolute path to the public certificate file to use for signing
?  ------------
+ # Absolute path to the public certificate file to use for signing responses to
?                                                                  +++++++++++++
- # PKI and PKIZ tokens. Set this together with `[signing] keyfile`. For non-
+ # revocation lists requests. Set this together with `[signing] keyfile`. For
- # production environments, you may be interested in using `keystone-manage
+ # non-production environments, you may be interested in using `keystone-manage
?   ++++
+ # pki_setup` to generate self-signed certificates. (string value)
- # pki_setup` to generate self-signed certificates. There is no reason to set
- # this option unless you are using either a `pki` or `pkiz` `[token] provider`.
- # (string value)
- # This option is deprecated for removal since M.
- # Its value may be silently ignored in the future.
- # Reason: PKI token support has been deprecated in the M release and will be
- # removed in the O release. Fernet or UUID tokens are recommended.
  # certfile = /etc/keystone/ssl/certs/signing_cert.pem

* key_size
- # DEPRECATED: Key size (in bits) to use when generating a self-signed token
?  ------------
+ # Key size (in bits) to use when generating a self-signed token signing
?                                                                ++++++++
- # signing certificate. There is no reason to set this option unless you are
?  --------
+ # certificate. There is no reason to set this option unless you are requesting
?                                                                    +++++++++++
+ # revocation lists in a non-production environment. Use a `[signing] certfile`
+ # issued from a trusted certificate authority instead. (integer value)
- # using a `pki` or `pkiz` `[token] provider` value in a non-production
- # environment. Use a `[signing] certfile` issued from a trusted certificate
- # authority instead. (integer value)
  # Minimum value: 1024
- # This option is deprecated for removal since M.
- # Its value may be silently ignored in the future.
- # Reason: PKI token support has been deprecated in the M release and will be
- # removed in the O release. Fernet or UUID tokens are recommended.
  # key_size = 2048

* keyfile
- # DEPRECATED: Absolute path to the private key file to use for signing PKI and
?  ------------                                                          ^^^^^ ^
+ # Absolute path to the private key file to use for signing responses to
?                                                            ^^^^^ ^^^^^^
+ # revocation lists requests. Set this together with `[signing] certfile`.
- # PKIZ tokens. Set this together with `[signing] certfile`. There is no reason
- # to set this option unless you are using either a `pki` or `pkiz` `[token]
- # provider`. (string value)
?  -----------
+ # (string value)
- # This option is deprecated for removal since M.
- # Its value may be silently ignored in the future.
- # Reason: PKI token support has been deprecated in the M release and will be
- # removed in the O release. Fernet or UUID tokens are recommended.
  # keyfile = /etc/keystone/ssl/private/signing_key.pem

* valid_days
- # DEPRECATED: The validity period (in days) to use when generating a self-
?  ------------
+ # The validity period (in days) to use when generating a self-signed token
?                                                               ++++++++++++
- # signed token signing certificate. There is no reason to set this option
?  -------------
+ # signing certificate. There is no reason to set this option unless you are
?                                                             +++++++++++++++
+ # requesting revocation lists in a non-production environment. Use a `[signing]
+ # certfile` issued from a trusted certificate authority instead. (integer
+ # value)
- # unless you are using a `pki` or `pkiz` `[token] provider` value in a non-
- # production environment. Use a `[signing] certfile` issued from a trusted
- # certificate authority instead. (integer value)
- # This option is deprecated for removal since M.
- # Its value may be silently ignored in the future.
- # Reason: PKI token support has been deprecated in the M release and will be
- # removed in the O release. Fernet or UUID tokens are recommended.
  # valid_days = 3650

* driver
  # Entry point for the token persistence backend driver in the
- # `keystone.token.persistence` namespace. Keystone provides `kvs`, `memcache`,
?                                                                  ^  ^^^^^^^^ -
+ # `keystone.token.persistence` namespace. Keystone provides `kvs` and `sql`
?                                                                  ^^^^  ^^^
+ # drivers. The `kvs` backend depends on the configuration in the `[kvs]`
+ # section. The `sql` option (default) depends on the options in your
+ # `[database]` section. If you're using the `fernet` `[token] provider`, this
- # `memcache_pool`, and `sql` drivers. The `kvs` backend depends on the
- # configuration in the `[kvs]` section. The `memcache` and `memcache_pool`
- # options depend on the configuration in the `[memcache]` section. The `sql`
- # option (default) depends on the options in your `[database]` section. If
- # you're using the `fernet` `[token] provider`, this backend will not be
- # utilized to persist tokens at all. (string value)
+ # backend will not be utilized to persist tokens at all. (string value)
?  ++++++++++++++++++++
  # driver = sql


-------------------------
```
