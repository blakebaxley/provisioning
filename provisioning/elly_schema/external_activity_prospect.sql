CREATE TABLE `external_activity_prospect` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `account_id` int(11) unsigned NOT NULL,
  `prospect_id` int(10) unsigned NOT NULL,
  PRIMARY KEY (`id`),
  KEY `external_activity_prospect_account_id_prospect_id` (`account_id`,`prospect_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
