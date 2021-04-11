CREATE TABLE `external_activity_request` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `account_id` int(11) unsigned NOT NULL,
  `created_by` int(11) unsigned NOT NULL,
  `created_at` datetime NOT NULL,
  `success` tinyint(1) DEFAULT NULL,
  `extension_fid` char(18) DEFAULT NULL,
  `external_activity_type_fid` char(18) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `external_activity_request_account_id_created_at` (`account_id`,`created_at`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;