/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50716
Source Host           : localhost:3306
Source Database       : flexsafe

Target Server Type    : MYSQL
Target Server Version : 50716
File Encoding         : 65001

Date: 2016-12-27 10:31:19
*/
DROP FUNCTION IF EXISTS http_get;
DROP FUNCTION IF EXISTS http_post;
DROP FUNCTION IF EXISTS http_put;
DROP FUNCTION IF EXISTS http_delete;
create function http_get returns string soname 'mysql-udf-http.so';
create function http_post returns string soname 'mysql-udf-http.so';
create function http_put returns string soname 'mysql-udf-http.so';
create function http_delete returns string soname 'mysql-udf-http.so';

/*DROP DATABASE IF EXISTS flexsafe;*/
CREATE DATABASE IF NOT EXISTS flexsafe;
use flexsafe;

SET FOREIGN_KEY_CHECKS=0;
SET character_set_client='utf8';
SET character_set_database='utf8';
SET character_set_server='utf8';

-- ----------------------------
-- Table structure for `account_info`
-- ----------------------------
/*DROP TABLE IF EXISTS `account_info`;*/
CREATE TABLE IF NOT EXISTS `account_info` (
  `name` varchar(64) NOT NULL DEFAULT '',
  `unit` varchar(1024) NOT NULL DEFAULT '',
  `address` varchar(1024) NOT NULL DEFAULT '',
  `email` varchar(255) DEFAULT '',
  `account` varchar(64) NOT NULL DEFAULT '',
  `phone_num` varchar(64) NOT NULL DEFAULT '',
  `invoice_title` varchar(255) NOT NULL DEFAULT '',
  `pay_method` varchar(255) NOT NULL DEFAULT '',
  `agent` varchar(255) NOT NULL DEFAULT '',
  `agent_email` varchar(255) NOT NULL DEFAULT '',
  `activation_code` varchar(10) NOT NULL DEFAULT '',
  PRIMARY KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of account_info
-- ----------------------------

-- ----------------------------
-- Table structure for `backup_config`
-- ----------------------------
/*DROP TABLE IF EXISTS `backup_config`;*/
CREATE TABLE IF NOT EXISTS `backup_config` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(64) NOT NULL DEFAULT '',
  `server_ip` varchar(64) NOT NULL DEFAULT '',
  `backup_server_type` tinyint(1) DEFAULT '0' COMMENT '备份服务器类型:0:本地;1:云端;',
  `access_id` varchar(50) DEFAULT '' COMMENT '如果是云端，需要设置access_id',
  `access_key` varchar(50) DEFAULT '' COMMENT '如果是云端，需要设置access_key',
  `uuid` varchar(32) DEFAULT '',
  `status` tinyint(1) DEFAULT '1' COMMENT '状态:0:关闭;1:开启;',
  PRIMARY KEY (`id`),
  UNIQUE KEY `index_server_ip` (`server_ip`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of backup_config
-- ----------------------------

-- ----------------------------
-- Table structure for `backup_item`
-- ----------------------------
/*DROP TABLE IF EXISTS `backup_item`;*/
CREATE TABLE `backup_item` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT '',
  `type` int(4) NOT NULL DEFAULT '0' COMMENT '0:逻辑卷;1:用户;2:系统;3:目录;4:文件;',
  `src_id` varchar(512) NOT NULL DEFAULT '',
  `file_path` varchar(255) DEFAULT '' COMMENT '用户指定目录/文件备份路径',
  `special_path` tinyint(1) DEFAULT '0' COMMENT '特殊路径:0:否;1:是;',
  `backup_interval` int(11) DEFAULT '0' COMMENT '备份周期',
  `backup_time` varchar(25) DEFAULT '' COMMENT '备份时间',
  `reserved_cnt` int(11) DEFAULT '0' COMMENT '保留备份数',
  `incremental_cnt` int(11) DEFAULT '0' COMMENT '增量备份数',
  `backup_config_id` int(11) NOT NULL DEFAULT '0',
  `backup_count` int(11) DEFAULT '0' COMMENT '备份次数',
  `object_status` tinyint(1) DEFAULT '1' COMMENT '对象状态:0:删除;1:正常;逻辑卷和用户可能存在被删除的情况',
  `status` tinyint(1) DEFAULT '1' COMMENT '状态:0:关闭;1:开启;',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of backup_item
-- ----------------------------

-- ----------------------------
-- Table structure for `email`
-- ----------------------------
/*DROP TABLE IF EXISTS `email`;*/
CREATE TABLE `email` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL DEFAULT '0',
  `remote_user_id` int(11) DEFAULT '0',
  `code` varchar(15) NOT NULL DEFAULT '' COMMENT '信息类型',
  `level` tinyint(1) NOT NULL DEFAULT '0' COMMENT '信息级别',
  `params` varchar(1000) NOT NULL DEFAULT '' COMMENT '信息内容',
  `send_count` tinyint(1) NOT NULL DEFAULT '0' COMMENT '发送次数',
  `add_time` int(11) DEFAULT '0' COMMENT '添加时间',
  `status` tinyint(1) DEFAULT '0' COMMENT '信息是否发送:0(未发送),1(已发送);',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
-- ----------------------------
-- Records of email
-- ----------------------------

-- ----------------------------
-- Table structure for `email_history`
-- ----------------------------
/*DROP TABLE IF EXISTS `email_history`;*/
CREATE TABLE `email_history` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `email_id` int(11) NOT NULL DEFAULT '0',
  `user_id` int(11) NOT NULL DEFAULT '0',
  `code` varchar(15) NOT NULL DEFAULT '' COMMENT '信息类型',
  `level` tinyint(1) NOT NULL DEFAULT '0' COMMENT '信息级别',
  `params` varchar(1000) NOT NULL DEFAULT '' COMMENT '信息内容',
  `send_count` tinyint(1) NOT NULL DEFAULT '0' COMMENT '发送次数',
  `add_time` int(11) DEFAULT '0' COMMENT '添加时间',
  `send_time` int(11) DEFAULT '0' COMMENT '发送时间',
  `status` tinyint(1) DEFAULT '0' COMMENT '信息是否发送:0(未发送)，1(已发送);',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
-- ----------------------------
-- Records of email_history
-- ----------------------------

-- ----------------------------
-- Table structure for `email_level`
-- ----------------------------
/*DROP TABLE IF EXISTS `email_level`;*/
CREATE TABLE `email_level` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `code` char(5) NOT NULL DEFAULT '' COMMENT '编码',
  `level` varchar(5) NOT NULL DEFAULT '' COMMENT '等级',
  `comment` varchar(255) DEFAULT '' COMMENT '注释',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=utf8;
-- ----------------------------
-- Records of email_level
-- ----------------------------

-- ----------------------------
-- Table structure for `message`
-- ----------------------------
/*DROP TABLE IF EXISTS `message`;*/
CREATE TABLE `message` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL DEFAULT '0',
  `remote_user_id` int(11) DEFAULT '0',
  `code` varchar(15) NOT NULL DEFAULT '' COMMENT '信息类型',
  `level` tinyint(1) NOT NULL DEFAULT '0' COMMENT '信息级别',
  `params` varchar(1000) NOT NULL DEFAULT '' COMMENT '信息内容',
  `add_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `status` tinyint(1) DEFAULT '0' COMMENT '状态:0(未读),1(已读);',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
-- ----------------------------
-- Records of message
-- ----------------------------

-- ----------------------------
-- Table structure for `message_last_time`
-- ----------------------------
/*DROP TABLE IF EXISTS `message_lastest_time`;*/
CREATE TABLE `message_lastest_time` (
  `user_id` int(11) NOT NULL DEFAULT '0',
  `lastest_time` timestamp NOT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
-- ----------------------------
-- Records of message_last_time
-- ----------------------------

-- ----------------------------
-- Table structure for `groups`
-- ----------------------------
/*DROP TABLE IF EXISTS `groups`;*/
CREATE TABLE IF NOT EXISTS `groups` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `parent` int(11) unsigned NOT NULL DEFAULT '0',
  `creator_id` int(11) unsigned NOT NULL DEFAULT '0',
  `creator` varchar(255) DEFAULT '',
  `display_name` varchar(255) DEFAULT '',
  `group_name` varchar(255) DEFAULT '',
  `group_title` varchar(255) DEFAULT '',
  `privilege` varchar(125) DEFAULT '',
  `lv_name` varchar(255) DEFAULT '',
  `root_directory` varchar(255) DEFAULT '',
  `add_time` int(11) DEFAULT '0',
  `default_group` tinyint(1) DEFAULT NULL,
  `deleted` tinyint(1) DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of groups
-- ----------------------------

-- ----------------------------
-- Table structure for `oc_filecache_tmp`
-- ----------------------------
/*DROP TABLE IF EXISTS `oc_filecache_tmp`;*/
CREATE TABLE IF NOT EXISTS `oc_filecache_tmp` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `user_title` varchar(50) NOT NULL DEFAULT '',
  `path` varchar(255) DEFAULT '',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of oc_filecache_tmp
-- ----------------------------

-- ----------------------------
-- Table structure for `user`
-- ----------------------------
/*DROP TABLE IF EXISTS `user`;*/
CREATE TABLE IF NOT EXISTS `user` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL DEFAULT '',
  `personal_name` varchar(50) NOT NULL DEFAULT '',
  `email` varchar(255) NOT NULL DEFAULT '',
  `password` varchar(50) DEFAULT '',
  `password_reserted` tinyint(1) DEFAULT '1',
  `password_encrypted` tinyint(1) DEFAULT '0',
  `user_title` varchar(255) DEFAULT '',
  `privilege` varchar(125) DEFAULT '',
  `layer` varchar(125) DEFAULT '',
  `lv_name` varchar(255) DEFAULT '',
  `root_directory` varchar(255) DEFAULT '',
  `max_size` int(11) DEFAULT '0' COMMENT '用户可用总空间，单位G',
  `used_size` bigint(20) DEFAULT '0' COMMENT '用户已用空间，单位B',
  `phone` varchar(50) DEFAULT '',
  `department` varchar(125) DEFAULT '',
  `add_time` int(11) DEFAULT '11',
  `take_over` tinyint(1) DEFAULT '0' COMMENT '托管:0(未托管);1(已托管);',
  `email_level` tinyint(1) DEFAULT '10' COMMENT '用户接受邮件级别:默认10，数字越低级别约高',
  `message_level` tinyint(1) DEFAULT '10' COMMENT '用户接受消息级别:默认10，数字越低级别约高',  
  `language_setting` tinyint(1) DEFAULT '0' COMMENT '用户语言:0(English);1(简体中文);2(繁体中文)',
  `duty` tinyint(1) DEFAULT '2' COMMENT '用户权限:0(超级管理员);1(二级管理员);2(普通用户);',
  `remote_user` tinyint(1) DEFAULT '0' COMMENT '远程用户:0(本地用户);1(主远程用户);2(从远程用户);',
  `remote_user_status` tinyint(1) DEFAULT '0' COMMENT '远程用户状态:0(无);1(正常);2(禁用);3(删除);',
  `disabled` tinyint(1) DEFAULT '0' COMMENT '用户禁用状态:0(正常);1(禁用)',
  `deleted` tinyint(1) DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

create index INDEX_NAME_PASSWORD on `user` (`username`, `password`);
-- ----------------------------
-- Records of user
-- ----------------------------

-- ----------------------------
-- Table structure for `user_group`
-- ----------------------------
/*DROP TABLE IF EXISTS `user_group`;*/
CREATE TABLE IF NOT EXISTS `user_group` (
  `user_id` int(11) NOT NULL DEFAULT '0',
  `group_id` int(11) NOT NULL DEFAULT '0',
  `permission` smallint(4) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of user_group
-- ----------------------------

-- ----------------------------
-- Table structure for `storage_planning`
-- ----------------------------
/*DROP TABLE IF EXISTS `storage_planning`;*/
CREATE TABLE IF NOT EXISTS `storage_planning` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL DEFAULT 0,
  `add_time` varchar(64) NOT NULL DEFAULT '',
  `used` varchar(256) NOT NULL DEFAULT '',
  `latest` int(2) NOT NULL DEFAULT 0,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
-- ----------------------------
-- Records of storage_planning
-- ----------------------------

-- ----------------------------
-- Table structure for `share_info`
-- ----------------------------
/*DROP TABLE IF EXISTS `share_dir`;*/
CREATE TABLE IF NOT EXISTS `share_dir` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL DEFAULT 0,
  `creator_id` int(11) unsigned NOT NULL DEFAULT '0',
  `creator` varchar(255) DEFAULT '',
  `boxsafe_initiator` varchar(64) NOT NULL DEFAULT '',
  `boxsafe_filecache_id` int(11) NOT NULL DEFAULT 0,
  `share_name` varchar(64) NOT NULL DEFAULT '',
  `share_path` varchar(256) NOT NULL DEFAULT '',
  `link_name` varchar(64) NOT NULL DEFAULT '',
  `max_size` bigint(20) NOT NULL DEFAULT 0,
  `dir_model` tinyint(20) NOT NULL DEFAULT '0' COMMENT '目录模式:0:个人模式， 1:协作模式， 2:公共模式;',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
-- ----------------------------
-- Records of share_dir
-- ----------------------------

-- ----------------------------
-- Table structure for `share_owner`
-- ----------------------------
/*DROP TABLE IF EXISTS `share_owner`;*/
CREATE TABLE IF NOT EXISTS `share_owner` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL DEFAULT 0,
  `file_id` int(11) NOT NULL DEFAULT 0,
  `share_id` int(11) NOT NULL DEFAULT 0,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
-- ----------------------------
-- Records of share_owner
-- ----------------------------

-- ----------------------------
-- Table structure for `logs`
-- ----------------------------
/*DROP TABLE IF EXISTS `logs`;*/
CREATE TABLE IF NOT EXISTS `logs` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `cmd` varchar(50) NOT NULL DEFAULT '',
  `opt` varchar(50) NOT NULL DEFAULT '',
  `message` varchar(255) NOT NULL DEFAULT '',
  `add_time` int(11) NOT NULL DEFAULT '0',
  `type` tinyint(1) NOT NULL DEFAULT '1' COMMENT '日志类型:1:web操作日志;',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
-- ----------------------------
-- Records of logs
-- ----------------------------

-- ----------------------------
-- Table structure for `archive_dir`
-- ----------------------------
/*DROP TABLE IF EXISTS `archive_dir`;*/

CREATE TABLE IF NOT EXISTS `archive_dir` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `creator_id` int(11) NOT NULL DEFAULT 0,
  `initiator` varchar(120) NOT NULL,
  `shareWith_id` int(11) NOT NULL DEFAULT 0,
  `shareWith` varchar(120) NOT NULL,
  `boxsafe_filecache_id` int(11) NOT NULL,
  `share_path` varchar(250) NOT NULL,
  `share_name` varchar(100) NOT NULL,
  `share_type` int(11) DEFAULT NULL,
  `max_size` bigint(20) NOT NULL DEFAULT 0,
  `permission` int(11) DEFAULT '1',
  KEY `id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of archive dir
-- ----------------------------

-- ----------------------------
-- Table structure for `file_activity`
-- ----------------------------
/*DROP TABLE IF EXISTS `file_activity`;*/
CREATE TABLE IF NOT EXISTS `file_activity` (
  `activity_id` int(11) NOT NULL AUTO_INCREMENT,
  `timestamp` int(11) NOT NULL DEFAULT '0',
  `priority` int(11) NOT NULL DEFAULT '0',
  `type` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  `user` varchar(64) COLLATE utf8_bin DEFAULT NULL,
  `affecteduser` varchar(64) COLLATE utf8_bin NOT NULL,
  `app` varchar(255) COLLATE utf8_bin NOT NULL,
  `subject` varchar(255) COLLATE utf8_bin NOT NULL,
  `subjectparams` varchar(4000) COLLATE utf8_bin NOT NULL,
  `message` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  `messageparams` varchar(4000) COLLATE utf8_bin DEFAULT NULL,
  `file` varchar(4000) COLLATE utf8_bin DEFAULT NULL,
  `link` varchar(4000) COLLATE utf8_bin DEFAULT NULL,
  `object_type` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  `object_id` int(11) NOT NULL DEFAULT '0',
  `displayed` tinyint(1) DEFAULT '0',
  PRIMARY KEY (`activity_id`),
  KEY `activity_time` (`timestamp`),
  KEY `activity_user_time` (`affecteduser`,`timestamp`),
  KEY `activity_filter_by` (`affecteduser`,`user`,`timestamp`),
  KEY `activity_filter_app` (`affecteduser`,`app`,`timestamp`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
-- ----------------------------
-- Records of file_activity
-- ----------------------------

-- ----------------------------
-- Table structure for `file_preview`
-- ----------------------------
DROP TABLE IF EXISTS `file_preview`;
CREATE TABLE `file_preview` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `file_id` int(11) NOT NULL DEFAULT '0',
  `page_number` int(11) DEFAULT '0',
  `add_time` int(11) DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
-- ----------------------------
-- Records of file_preview
-- ----------------------------

-- ----------------------------
-- Table structure for `file_lock`
-- ----------------------------
CREATE TABLE `file_lock` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `user_id` int(11) unsigned NOT NULL DEFAULT '0',
  `username` varchar(25) DEFAULT '',
  `file_id` int(11) DEFAULT '0',
  `file_name` varchar(255) DEFAULT '',
  `channel` tinyint(1) NOT NULL DEFAULT '1' COMMENT '渠道:1(web);2(android);3(ios);',
  `add_time` int(11) DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
-- ----------------------------
-- Records of file_lock
-- ----------------------------

-- ----------------------------
-- Table structure for `file_unlock_code`
-- ----------------------------
CREATE TABLE `file_unlock_code` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT '0',
  `file_lock_id` int(11) NOT NULL DEFAULT '0',
  `code` char(4) NOT NULL,
  `status` tinyint(1) DEFAULT '0' COMMENT '状态:0(未使用);1(已使用);2(已失效);',
  `add_time` int(11) DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
-- ----------------------------
-- Records of file_unlock_code
-- ----------------------------

-- ----------------------------
-- Table structure for `take_over_user_file_archive`
-- ----------------------------
DROP TABLE IF EXISTS `take_over_user_file_archive`;
CREATE TABLE `take_over_user_file_archive` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL DEFAULT '0',
  `filepath` varchar(255) NOT NULL DEFAULT '',
  `add_time` int(11) DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
-- ----------------------------
-- Records of take_over_user_file_archive
-- ----------------------------

-- ----------------------------
-- Table structure for `system_settings_shutdown`
-- ----------------------------
DROP TABLE IF EXISTS `system_settings_shutdown`;
CREATE TABLE `system_settings_shutdown` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `cmd` varchar(25) DEFAULT '',
  `opt` varchar(125) DEFAULT '',
  `exec_time` varchar(25) DEFAULT '',
  `add_time` int(11) DEFAULT '0',
  `deleted` tinyint(1) DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
-- ----------------------------
-- Records of system_settings_shutdown
-- ----------------------------

-- ----------------------------
-- Table structure for `system_config`
-- ----------------------------
/*DROP TABLE IF EXISTS `system_config`;*/
CREATE TABLE IF NOT EXISTS `system_config` (
  `name` varchar(125) NOT NULL DEFAULT '',
  `value` varchar(125) NOT NULL DEFAULT '',
  `comment` varchar(125) DEFAULT '',
  PRIMARY KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
INSERT INTO system_config(`name`, `value`, `comment`) VALUES('global.user.email.update.enable', '1', 'allow users to modify email information, 0:no 1:yes');
INSERT INTO system_config(`name`, `value`, `comment`) VALUES('global.user.phone.update.enable', '1', 'allow users to modify phone information, 0:no 1:yes');
INSERT INTO system_config(`name`, `value`, `comment`) VALUES('global.user.department.update.enable', '1', 'allow users to modify department information, 0:no 1:yes');
INSERT INTO system_config(`name`, `value`, `comment`) VALUES('global.system.message.sender.enable', '1', 'choose message sender mode, 0:close 1:email sender 2:message push');
INSERT INTO system_config(`name`, `value`, `comment`) VALUES('global.adminuser.create.linuxuser.enable', '0', 'does the administrator create a linux user, 0:no 1:yes');
INSERT INTO system_config(`name`, `value`, `comment`) VALUES('global.system.language', '1', 'system default language 0:english 1:simplified Chinese 2:traditional Chinese');
INSERT INTO system_config(`name`, `value`, `comment`) VALUES('global.system.intranet.ip', '', 'Intranet IP address');
INSERT INTO system_config(`name`, `value`, `comment`) VALUES ('global.system.intranet.port', '8080', '');
INSERT INTO system_config(`name`, `value`, `comment`) VALUES('global.system.extranet.ip', '', 'extranet IP address');
INSERT INTO system_config(`name`, `value`, `comment`) VALUES ('global.system.extranet.port', '8080', '');
INSERT INTO system_config(`name`, `value`, `comment`) VALUES('global.system.domain.name', '', 'Domain Name');
INSERT INTO system_config(`name`, `value`, `comment`) VALUES ('global.system.domain.http.port', '8080', 'Doamin http port 8080');
INSERT INTO system_config(`name`, `value`, `comment`) VALUES('global.system.masterslave.type','1','system master slave type, 0:slave 1:master');
INSERT INTO system_config(`name`, `value`, `comment`) VALUES('global.system.server.version','1.9.5alpha','flexsafe version');
INSERT INTO system_config(`name`, `value`, `comment`) VALUES('global.system.smtp','1','smtp serve set prompt or not  ,0: prompt  1: not prompt');
INSERT INTO system_config(`name`, `value`, `comment`) VALUES('global.user.enter.wrong.password.numbers.lock.account', '3', 'The user entered the wrong number of passwords, locked the account, the default 3 times');
INSERT INTO system_config(`name`, `value`, `comment`) VALUES('global.user.account.lockout.time', '1800', 'User misplaced password account lock time, unit is second');
INSERT INTO system_config(`name`, `value`, `comment`) VALUES ('global.system.send.p1.mail.interval.timer', '5', 'send p1 email interval timer 5 minutes');
INSERT INTO system_config(`name`, `value`, `comment`) VALUES ('global.system.send.p10.mail.interval.timer', '5', 'send p10 email interval timer 5 minutes');
INSERT INTO system_config(`name`, `value`, `comment`) VALUES ('global.system.send.p1.mail.timer', '30', '');
INSERT INTO system_config(`name`, `value`, `comment`) VALUES ('global.system.send.p10.mail.timer', '60', '');
INSERT INTO system_config(`name`, `value`, `comment`) VALUES ('global.system.default.send.mail.count', '10', 'default batch send email count is 10');
INSERT INTO system_config(`name`, `value`, `comment`) VALUES('global.file.preview.type','pdf','File preview open type:openoffice,pdf');
INSERT INTO system_config(`name`, `value`, `comment`) VALUES('global.file.preview.user.rights','0','User access rights');
INSERT INTO system_config(`name`, `value`, `comment`) VALUES('global.file.preview.user.search.input.type','0','Search input type,0:scanner,1:handwrite and scanner');
INSERT INTO system_config(`name`, `value`, `comment`) VALUES ('global.system.network.protocol', 'http', 'system net work protocol:http or https');
INSERT INTO system_config(`name`, `value`, `comment`) VALUES ('global.system.file.lock.status', '1', 'file lock status: 0:no 1:yes'); 
INSERT INTO system_config(`name`, `value`, `comment`) VALUES ('global.system.domain.https.port', '443', 'Doamin https port 443'); 
INSERT INTO system_config(`name`, `value`, `comment`) VALUES ('global.system.uuid', '', 'global system uuid'); 

-- ----------------------------
-- Records of system_config
-- ----------------------------

-- ----------------------------
-- Table structure for `remote_broadcast_file`
-- ----------------------------
/*DROP TABLE IF EXISTS `remote_broadcast_file`;*/
CREATE TABLE `remote_broadcast_file` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `file_id` int(11) NOT NULL DEFAULT '0',
  `remote_user_id` int(11) NOT NULL DEFAULT '0',
  `finished` tinyint(1) DEFAULT '0',
  `add_time` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
-- ----------------------------
-- Records of remote_broadcast_file
-- ----------------------------

-- ----------------------------
-- Table structure for `remote_email`
-- ----------------------------
/*DROP TABLE IF EXISTS `remote_email`;*/
CREATE TABLE `remote_email` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `remote_user_id` int(11) NOT NULL DEFAULT '0',
  `username` varchar(50) NOT NULL DEFAULT '',
  `email` varchar(255) NOT NULL DEFAULT '',
  `content` varchar(255) DEFAULT '',
  `add_time` int(11) DEFAULT '0',
  `deleted` tinyint(1) DEFAULT '0' COMMENT '是否失效:0(未失效)，1(已失效);',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
-- ----------------------------
-- Records of remote_email
-- ----------------------------

-- ----------------------------
-- Table structure for `remote_server`
-- ----------------------------
/*DROP TABLE IF EXISTS `remote_server`;*/
CREATE TABLE `remote_server` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `uuid` varchar(32) DEFAULT '',
  `name` varchar(255) DEFAULT '',
  `intranet_ip` varchar(25) DEFAULT '',
  `intranet_port` varchar(25) DEFAULT '',
  `extranet_ip` varchar(25) DEFAULT '',
  `extranet_port` varchar(25) DEFAULT '',
  `domain` varchar(125) DEFAULT '',
  `domain_port` varchar(25) DEFAULT '',
  `user_id` int(11) DEFAULT '0',
  `origin` tinyint(1) DEFAULT '0',
  `add_time` int(11) NOT NULL DEFAULT '0',
  `deleted` tinyint(1) DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
-- ----------------------------
-- Records of remote_server
-- ----------------------------

-- ----------------------------
-- Table structure for `remote_user`
-- ----------------------------
/*DROP TABLE IF EXISTS `remote_user`;*/
CREATE TABLE `remote_user` (
   `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT '',
  `uuid` varchar(32) DEFAULT '' COMMENT '用户唯一标识',
  `intranet_ip` varchar(25) DEFAULT '',
  `intranet_port` varchar(25) DEFAULT '',
  `extranet_ip` varchar(25) DEFAULT '',
  `extranet_port` varchar(25) DEFAULT '',
  `domain` varchar(125) DEFAULT '',
  `domain_port` varchar(25) NOT NULL DEFAULT '',
  `username` varchar(25) NOT NULL DEFAULT '',
  `email` varchar(125) DEFAULT '',
  `lv_name` varchar(255) DEFAULT '',
  `root_directory` varchar(255) DEFAULT '',
  `language` tinyint(1) DEFAULT '1',
  `verify` tinyint(1) DEFAULT '0' COMMENT '审核状态:0(未审核)，1(已激活)，2(激活失败)，3(已断开);',
  `status` tinyint(1) DEFAULT '0',
  `create_by` int(11) DEFAULT '0',
  `add_time` int(11) NOT NULL DEFAULT '0',
  `deleted` tinyint(1) DEFAULT '0' COMMENT '删除:0(未删除)，1(总部删除)，2(分部删除);',
  `email_level` tinyint(1) DEFAULT '10',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
-- ----------------------------
-- Records of remote_user
-- ----------------------------

-- ----------------------------
-- Table structure for `user_import`
-- ----------------------------
/*DROP TABLE IF EXISTS `user_import`;*/
CREATE TABLE `user_import` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `batch` varchar(25) NOT NULL DEFAULT '' COMMENT '导入批次',
  `username` varchar(50) NOT NULL DEFAULT '',
  `personal_name` varchar(50) DEFAULT '',
  `email` varchar(125) DEFAULT '',
  `password` varchar(50) DEFAULT '',
  `lv_name` varchar(255) DEFAULT '',
  `lv_size` varchar(255) DEFAULT '',
  `phone` varchar(25) DEFAULT '',
  `user_data_username` varchar(255) DEFAULT '',
  `user_data_password` varchar(255) DEFAULT '',
  `message` varchar(255) DEFAULT '' COMMENT '导入信息',
  `status` tinyint(1) DEFAULT '0' COMMENT '导入状态:0(未导入);1(导入成功);2(导入失败);',
  `add_time` int(11) DEFAULT '0',
  `end_time` int(11) DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
-- ----------------------------
-- Records of user_import
-- ----------------------------

-- ----------------------------
-- Table structure for `deleted_trash_files`
-- ----------------------------
drop table if exists `deleted_trash_files` ;
CREATE TABLE `deleted_trash_files` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `auto_id` int(11) COLLATE utf8_bin NOT NULL DEFAULT '0',
  `deleted_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `user` varchar(50) NOT NULL DEFAULT '',
  `trash_path` varchar(250) COLLATE utf8_bin NOT NULL DEFAULT '',
  PRIMARY KEY (`id`),
  KEY `auto_id_index` (`auto_id`),
  KEY `deleted_time_index` (`deleted_time`),
  KEY `user_trash_index` (`user`)
) ENGINE=InnoDB AUTO_INCREMENT=173 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
-- ----------------------------
-- Records of deleted_trash_files
-- ----------------------------

-- ----------------------------
-- Table structure for `permission_change`
-- ----------------------------
drop table if exists `permission_change` ;
CREATE TABLE `permission_change` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT '0',
  `file_id` int(11) DEFAULT '0',
  `remote_path` varchar(255) DEFAULT '',
  `permission` int(11) DEFAULT '0',
  `operate_time` int(11) DEFAULT '0',
  `operate_user` varchar(255) DEFAULT '',
  `operate_client` varchar(255) DEFAULT '',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
SELECT * FROM flexsafe.permission_change;
-- ----------------------------
-- Records of permission_change
-- ----------------------------

-- ----------------------------
-- Table structure for `file_change`
-- ----------------------------
drop table if exists `file_change` ;
CREATE TABLE `file_change` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `file_id` int(11) DEFAULT '0',
  `operate_type` varchar(25) DEFAULT '',
  `operate_time` int(11) DEFAULT '0',
  `operate_user` varchar(255) DEFAULT '',
  `operate_client` varchar(255) DEFAULT '',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
-- ----------------------------
-- Records of file_change
-- ----------------------------

-- ----------------------------
-- Table structure for `varicut_contract_file`
-- ----------------------------
CREATE TABLE varicut_contract_file
(
  id                      INT AUTO_INCREMENT
  PRIMARY KEY,
  username                VARCHAR(50) DEFAULT ''   NULL,
  boxsafe_id              INT                      NOT NULL,
  file_path               VARCHAR(1000) DEFAULT '' NULL,
  control_file_type       VARCHAR(50) DEFAULT ''   NOT NULL COMMENT '管控文件类型',
  supplier                VARCHAR(255) DEFAULT ''  NOT NULL COMMENT '供应商',
  signing_date            VARCHAR(25) DEFAULT ''   NULL COMMENT '签订日期',
  expire_date             VARCHAR(25) DEFAULT ''   NULL COMMENT '到期日期',
  internal_contacts_name  VARCHAR(50) DEFAULT ''   NULL COMMENT '内部联系人',
  internal_contacts_email VARCHAR(500) DEFAULT ''  NULL COMMENT '内部联系人邮箱（可设置多个，中间,分隔）',
  internal_reminder_date  VARCHAR(25) DEFAULT ''   NULL COMMENT '内部提醒日期',
  external_contacts_name  VARCHAR(50) DEFAULT ''   NULL COMMENT '外部联系人',
  external_contacts_email VARCHAR(500) DEFAULT ''  NULL COMMENT '外部联系人邮箱（可设置多个，中间,分隔）',
  external_reminder_date  VARCHAR(50) DEFAULT ''   NULL COMMENT '外部提醒日期',
  email_reminder          TINYINT(1) DEFAULT '1'   NULL COMMENT '邮件提醒:0(未开启);1(开启)',
  add_time                INT DEFAULT '0'          NOT NULL,
  deleted                 TINYINT(1) DEFAULT '0'   NULL COMMENT '是否删除:0(正常);1(删除)'
)ENGINE=InnoDB DEFAULT CHARSET=utf8;
-- ----------------------------
-- Records of varicut_contract_file
-- ----------------------------

-- ----------------------------
-- Function structure for `get_dir_share`
-- ----------------------------
DROP FUNCTION IF EXISTS `get_dir_share`;
DELIMITER $$
CREATE DEFINER=`root`@`localhost` FUNCTION `get_dir_share`(
    in_share_with VARCHAR(256) CHARACTER SET utf8,
    in_file_path VARCHAR(2048) CHARACTER SET utf8
    ) RETURNS INT(11)
BEGIN
      DECLARE i_file_cache_id INT DEFAULT -1;
      DECLARE i_file_source_id INT DEFAULT -1;
      DECLARE s_sharepath VARCHAR(2048) CHARACTER SET utf8;
      DECLARE s_subsharepath VARCHAR(2048) CHARACTER SET utf8;
      DECLARE i_sharestorage INT DEFAULT -1;
      
      SET s_subsharepath = in_file_path;
      
      loop1:LOOP
        SET s_subsharepath = REVERSE(SUBSTRING(REVERSE(s_subsharepath), INSTR(REVERSE(s_subsharepath), "/")+1));
        IF (s_subsharepath = "") THEN
          LEAVE loop1;
        END IF;
        
        SELECT `file_source` INTO i_file_source_id FROM `flexsafe`.`v_oc_share` WHERE `share_with`=in_share_with AND `file_target`=s_subsharepath;
        IF (i_file_source_id>0) THEN
          LEAVE loop1;
        END IF;
        
      END LOOP;

      IF (i_file_source_id>0) THEN
        SET s_sharepath=(CONCAT((SELECT `path` FROM `flexsafe`.`v_oc_filecache` WHERE fileid=i_file_source_id), SUBSTRING(in_file_path ,-(INSTR(REVERSE(in_file_path), REVERSE(s_subsharepath))-1))));
        SELECT `storage` INTO i_sharestorage FROM `flexsafe`.`v_oc_filecache` WHERE fileid=i_file_source_id;
        SELECT `fileid` INTO i_file_cache_id FROM `flexsafe`.`v_oc_filecache` f WHERE `storage`=i_sharestorage AND `path`=s_sharepath;
      END IF;
      RETURN (i_file_cache_id);
      END$$
DELIMITER ;
-- ----------------------------
-- Function structure for `get_dir_share`
-- ----------------------------

-- ----------------------------
-- Function structure for `get_file_share`
-- ----------------------------
DROP FUNCTION IF EXISTS `get_file_share`;
DELIMITER $$
CREATE DEFINER=`root`@`localhost` FUNCTION `get_file_share`(
    in_share_with VARCHAR(256) CHARACTER SET utf8,
    in_file_path VARCHAR(2048) CHARACTER SET utf8
    ) RETURNS INT(11)
BEGIN
      DECLARE i_file_source_id INT DEFAULT -1;
      SELECT `file_source` INTO i_file_source_id FROM `flexsafe`.`v_oc_share` WHERE `share_with`=in_share_with AND `file_target`=in_file_path;
      RETURN (i_file_source_id);
    END$$

DELIMITER ;
-- ----------------------------
-- Function structure for `get_file_share`
-- ----------------------------

-- ----------------------------
-- Function structure for `get_file_source`
-- ----------------------------
DROP FUNCTION IF EXISTS `get_file_source`;
DELIMITER $$
CREATE DEFINER=`root`@`localhost` FUNCTION `get_file_source`(
    in_username VARCHAR(256) CHARACTER SET utf8,
    in_filepath VARCHAR(2048) CHARACTER SET utf8
    ) RETURNS INT(11)
BEGIN
    DECLARE i_file_cache_id INT DEFAULT -1;
    DECLARE s_group_name VARCHAR(256) CHARACTER SET utf8;
    DECLARE done INT DEFAULT 0;
    DECLARE group_names CURSOR FOR SELECT group_name FROM groups WHERE deleted=0 AND id IN (SELECT group_id FROM user_group WHERE user_id=(SELECT user_id FROM `user` WHERE username=in_username AND deleted=0));
    
    SELECT `fileid` INTO i_file_cache_id FROM `flexsafe`.`v_oc_filecache` WHERE `storage`=(SELECT numeric_id FROM `flexsafe`.`v_oc_storages` WHERE id=CONCAT("home::", in_username)) AND `path`=CONCAT("files", in_filepath);
    IF (i_file_cache_id<0) THEN
      SET i_file_cache_id=get_file_share(in_username, in_filepath);
      IF (i_file_cache_id<0) THEN
        SET i_file_cache_id=get_dir_share(in_username, in_filepath);
        IF (i_file_cache_id<0) THEN
          OPEN group_names;
          myloop:LOOP
            IF done=1 THEN
              LEAVE myloop;
            END IF;
            FETCH group_names INTO s_group_name;

            SET i_file_cache_id=get_file_share(s_group_name, in_filepath);
            IF (i_file_cache_id<0) THEN
              SET i_file_cache_id=get_dir_share(s_group_name, in_filepath);
              IF (i_file_cache_id>0) THEN
                SET done = 1;
              END IF;
            ELSE
              SET done = 1;
            END IF;
          END LOOP;
          CLOSE group_names;
        END IF;
      END IF;
    END IF;
    RETURN (i_file_cache_id);
    END$$
DELIMITER ;
-- ----------------------------
-- Function structure for `get_file_source`
-- ----------------------------

-- ----------------------------
-- Function structure for `URL_DECODE`
-- ----------------------------
DROP FUNCTION IF EXISTS URL_DECODE;
DELIMITER $$
CREATE FUNCTION URL_DECODE (
    in_url VARCHAR(2048) CHARACTER SET utf8
) RETURNS VARCHAR(2048) CHARACTER SET utf8
BEGIN 
    DECLARE result VARCHAR(2048) CHARACTER SET utf8;
    DECLARE subresult VARCHAR(3) CHARACTER SET utf8;
    DECLARE pos INT DEFAULT 0;
    DECLARE length INT DEFAULT 0;
    SET result = REPLACE(in_url, '+', ' ');
    SET result = SUBSTRING_INDEX(result, ' HTTP', 1);
    SET result = SUBSTRING_INDEX(result, ' ', -1);

    SET pos = INSTR(result,"%"); 
    WHILE pos > 0 DO
       SET length = 3;
       SET subresult = substring(result, pos+3, 1);
       WHILE subresult = "%" DO
            SET length = length + 3;
            SET subresult = substring(result, pos+length, 1);
       END WHILE;
         
       SET result = CONCAT(substring(result, 1, pos-1), UNHEX(REPLACE(substring(result, pos, length),"%", "")), substring(result, pos+length));
       SET pos = INSTR(result,"%");
    END WHILE;

    RETURN result;
END$$
DELIMITER ;
-- ----------------------------
-- Function structure for `URL_DECODE`
-- ----------------------------

-- ----------------------------
-- Procudure structure for `anasys_apache2_log`
-- ----------------------------
DROP PROCEDURE IF EXISTS `anasys_apache2_log`;
DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `anasys_apache2_log`(
  in_username VARCHAR(256) CHARACTER SET utf8,
  in_method VARCHAR(15) CHARACTER SET utf8,
  in_ip VARCHAR(15) CHARACTER SET utf8,
  in_url VARCHAR(2048) CHARACTER SET utf8,
  in_agent VARCHAR(256) CHARACTER SET utf8,
  in_status VARCHAR(3) CHARACTER SET utf8
)
BEGIN
  DECLARE i_file_cache_id INT DEFAULT -1;
  DECLARE s_filepath VARCHAR(2048) CHARACTER SET utf8;
  DECLARE s_affendusername VARCHAR(256) CHARACTER SET utf8;

  IF in_method="GET" AND INSTR(in_url,"/remote.php/webdav")>0 THEN
    SET s_filepath=SUBSTRING(in_url, 19);
    SET i_file_cache_id=get_file_source(in_username,s_filepath);
    IF i_file_cache_id>0 THEN
      SELECT `id` INTO s_affendusername FROM `flexsafe`.`v_oc_storages` WHERE `numeric_id`= (SELECT `storage` from `flexsafe`.`v_oc_filecache` where `fileid`=i_file_cache_id);
      set s_affendusername=SUBSTRING_INDEX(s_affendusername, 'home::', -1);
      if s_affendusername=in_username then
        INSERT INTO `flexsafe`.`file_activity`(`timestamp`, `priority`, `type`, `user`, `affecteduser`, `app`, `subject`, `subjectparams`, `message`, `messageparams`,`file`, `link`, `object_type`, `object_id`) 
        VALUES (UNIX_TIMESTAMP(), 30, 'file_download', in_username, s_affendusername, 'files', 'download_self', '', '', '', s_filepath, in_url, 'files', i_file_cache_id);
      else
        INSERT INTO `flexsafe`.`file_activity`(`timestamp`, `priority`, `type`, `user`, `affecteduser`, `app`, `subject`, `subjectparams`, `message`, `messageparams`,`file`, `link`, `object_type`, `object_id`) 
        VALUES (UNIX_TIMESTAMP(), 30, 'file_download', in_username, s_affendusername, 'files', 'download_by', '', '', '', s_filepath, in_url, 'files', i_file_cache_id);
      end if;
    END IF;
  ELSEIF in_method="PUT" AND INSTR(in_url,"/remote.php/webdav")>0 THEN
    SET s_filepath=SUBSTRING(in_url, 19);
    SET i_file_cache_id=get_file_source(in_username,s_filepath);
    IF i_file_cache_id>0 THEN
      SELECT `id` INTO s_affendusername FROM `flexsafe`.`v_oc_storages` WHERE `numeric_id`= (SELECT `storage` FROM `flexsafe`.`v_oc_filecache` WHERE `fileid`=i_file_cache_id);
      SET s_affendusername=SUBSTRING_INDEX(s_affendusername, 'home::', -1);
      IF s_affendusername=in_username THEN
        INSERT INTO `flexsafe`.`file_activity`(`timestamp`, `priority`, `type`, `user`, `affecteduser`, `app`, `subject`, `subjectparams`, `message`, `messageparams`,`file`, `link`, `object_type`, `object_id`) 
        VALUES (UNIX_TIMESTAMP(), 30, 'file_upload', in_username, s_affendusername, 'files', 'upload_self', '', '', '', s_filepath, in_url, 'files', i_file_cache_id);
      ELSE
        INSERT INTO `flexsafe`.`file_activity`(`timestamp`, `priority`, `type`, `user`, `affecteduser`, `app`, `subject`, `subjectparams`, `message`, `messageparams`,`file`, `link`, `object_type`, `object_id`) 
        VALUES (UNIX_TIMESTAMP(), 30, 'file_upload', in_username, s_affendusername, 'files', 'upload_by', '', '', '', s_filepath, in_url, 'files', i_file_cache_id);
      END IF;
    END IF;
  END IF;
  END$$
DELIMITER ;
-- ----------------------------
-- Procudure structure for `anasys_apache2_log`
-- ----------------------------


-- ----------------------------
-- Trigger for message `tri_insert_message` `tri_update_message` `tri_delete_message`
-- ----------------------------
DROP TRIGGER IF EXISTS `tri_insert_message`;
DELIMITER ;;
CREATE TRIGGER `tri_insert_message` AFTER INSERT ON `message` FOR EACH ROW BEGIN
    REPLACE INTO message_lastest_time (user_id,lastest_time) VALUES(new.user_id, CURRENT_TIMESTAMP());
END
;;
DELIMITER ;

DROP TRIGGER IF EXISTS `tri_update_message`;
DELIMITER ;;
CREATE TRIGGER `tri_update_message` AFTER UPDATE ON `message` FOR EACH ROW begin
    REPLACE INTO message_lastest_time (user_id,lastest_time) VALUES(new.user_id, CURRENT_TIMESTAMP());
end
;;
DELIMITER ;

DROP TRIGGER IF EXISTS `tri_delete_message`;
DELIMITER ;;
CREATE TRIGGER `tri_delete_message` AFTER DELETE ON `message` FOR EACH ROW begin
    REPLACE INTO message_lastest_time (user_id,lastest_time) VALUES(old.user_id, CURRENT_TIMESTAMP());
end
;;
DELIMITER ;

-- ----------------------------
-- Trigger for message `tri_insert_message` `tri_update_message` `tri_delete_message`
-- ----------------------------











