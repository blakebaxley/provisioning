CREATE TABLE `external_activity` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `account_id` int(11) unsigned NOT NULL,
  `external_activity_type_fid` char(18) NOT NULL,
  `external_activity_prospect_id` bigint(20) unsigned NOT NULL,
  `value` varchar(255) DEFAULT NULL,
  `activity_date` datetime DEFAULT NULL,
  `created_by` int(11) unsigned NOT NULL,
  `created_at` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `external_activity_account_id_created_at` (`account_id`,`created_at`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
