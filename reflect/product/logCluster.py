import unittest
from po.config import ProductConfig
from po.utils.tools import datetime2timestamp


class OfflineClusterAnalysis:
    @classmethod
    def create_task(cls, **data):
        # 必填项
        name = data.get("name")
        dataSource_addressId = data.get("addressId")
        dataSource_to = datetime2timestamp(data.get("to"))
        dataSource_form = datetime2timestamp(data.get("form"))
        dataSource_index = data.get("index")

        # 扩展配置
        advanceConfig_anomalyIndexShards = data.get("anomalyIndexShards", 1)
        advanceConfig_dsGroups = data.get("dsGroups", [])
        advanceConfig_esIndexPattern = data.get("esIndexPattern", "unique")
        advanceConfig_executorNumber = data.get("executorNumber", 1)
        advanceConfig_logIndexShards = data.get("logIndexShards", 3)
        advanceConfig_outputVars = data.get("outputVars", False)
        advanceConfig_persistOption = data.get("persistOption", True)
        advanceConfig_spl = data.get("spl", "")
        advanceConfig_taskManagerMem = data.get("taskManagerMem", 2048)
        advanceConfig_contextField = data.get("contextField", "@rownumber")
        advanceConfig_contextFilterFields = data.get("contextFilterFields", "@path,@hostname")

        # 聚类设置
        aggregationConfig_enable = data.get("enable", True)
        aggregationConfig_windows = data.get("windows", 5)  # 聚类窗口 5 分钟

        # 关注模板
        attentionTemplates = data.get("attentionTemplates", [])

        # 聚类配置
        clusterConfig_format_rule = data.get("format_rule", "<content##[\s\S]*>")
        clusterConfig_replace_rule = data.get("replace_rule", [
            {'from': '\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}', 'to': '$DateTime'},
            {'from': 'https?://[^\s]+', 'to': '$URL'},
            {'from': '\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,5}', 'to': '$IPPort'},
            {'from': '\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', 'to': '$IP'},
            {'from': '(^|(?<=[^a-zA-Z\d\.]))\d+\.\d+(?=(\.?($|\s)|[^a-zA-Z\d\.]))',
             'to': '$NumFloat'}])
        clusterConfig_seperator_type = data.get("type", "RegExp")
        clusterConfig_seperator_value = data.get("value", "[^\w\u4e00-\u9fff\-/@]+")
        clusterConfig_keyword_type = data.get("type", "String")
        clusterConfig_keyword_value = data.get("value", "")
        clusterConfig_truncation = data.get("truncation", 100)
        clusterConfig_similarity = data.get("similarity", 0.5)
        clusterConfig_token_filter_ignore_digit = data.get("ignore_digit", False)
        clusterConfig_token_filter_ignore_replace_rule = data.get("ignore_replace_rule", False)

        # CMDB
        cmdbInfo_serviceName = data.get("serviceName", "")
        cmdbInfo_serviceId = data.get("serviceId", "")
        cmdbInfo_field = data.get("field", "")
        cmdbInfo_type = data.get("type", "dynamic")

        # 数据源
        dataSource_fieldName = data.get("fieldName", "@message")
        dataSource_previewCount = data.get("previewCount", 0)
        dataSource_timeField = data.get("timeField", "@timestamp")
        dataSource_timeFormat = data.get("timeFormat", "yyyy-MM-dd'T'HH:mm:ss.SSSZ")
        dataSource_timeZone = data.get("timeZone", "GMT+08:00")
        dataSource_type = data.get("type", "Elasticsearch")
        description = data.get("description", "this task created by auto test program")
        dataSource_sourceId = data.get("sourceId", 0)

        payload = {
            "advanceConfig": {
                "anomalyIndexShards": advanceConfig_anomalyIndexShards,
                "dsGroups": advanceConfig_dsGroups,
                "esIndexPattern": advanceConfig_esIndexPattern,
                "executorNumber": advanceConfig_executorNumber,
                "logIndexShards": advanceConfig_logIndexShards,
                "outputVars": advanceConfig_outputVars,
                "persistOption": advanceConfig_persistOption,
                "spl": advanceConfig_spl,
                "taskManagerMem": advanceConfig_taskManagerMem,
                "contextField": advanceConfig_contextField,
                "contextFilterFields": advanceConfig_contextFilterFields
            },
            "aggregationConfig": {
                "enable": aggregationConfig_enable,
                "windows": aggregationConfig_windows
            },
            "attentionTemplates": attentionTemplates,
            "clusterConfig": {
                "format_rule": clusterConfig_format_rule,
                "replace_rule": clusterConfig_replace_rule,
                "seperator": {
                    "type": clusterConfig_seperator_type,
                    "value": clusterConfig_seperator_value
                },
                "keyword": {
                    "type": clusterConfig_keyword_type,
                    "value": clusterConfig_keyword_value
                },
                "truncation": clusterConfig_truncation,
                "similarity": clusterConfig_similarity,
                "token_filter": {
                    "ignore_digit": clusterConfig_token_filter_ignore_digit,
                    "ignore_replace_rule": clusterConfig_token_filter_ignore_replace_rule
                }
            },
            "cmdbInfo": {
                "serviceName": cmdbInfo_serviceName,
                "serviceId": cmdbInfo_serviceId,
                "field": cmdbInfo_field,
                "type": cmdbInfo_type
            },
            "dataSource": {
                "fieldName": dataSource_fieldName,
                "form": dataSource_form,
                "index": dataSource_index,
                "previewCount": dataSource_previewCount,
                "sourceId": dataSource_sourceId,
                "timeField": dataSource_timeField,
                "timeFormat": dataSource_timeFormat,
                "timeZone": dataSource_timeZone,
                "to": dataSource_to,
                "type": dataSource_type,
                "addressId": dataSource_addressId
            },
            "description": description,
            "name": name
        }
        print(payload)


class RealtimeClusterAnalysis:
    @classmethod
    def create_task(cls, **data):
        # 必填项
        dataSource_topic = data.get("topic")
        dataSource_addressId = data.get("addressId")
        name = data.get("name", "name bak")

        # 扩展配置
        advanceConfig_filter = data.get("filter", "")  # uq过滤
        advanceConfig_anomalyIndexShards = data.get("anomalyIndexShards", 1)
        advanceConfig_clusterMsgMaxLength = data.get("clusterMsgMaxLength", 1000)
        advanceConfig_refreshInterval = data.get("refreshInterval", 5)
        advanceConfig_dsGroups = data.get("dsGroups", [])
        advanceConfig_esIndexPattern = data.get("esIndexPattern", "day")
        advanceConfig_executorNumber = data.get("executorNumber", 1)
        advanceConfig_logIndexShards = data.get("logIndexShards", 2)
        advanceConfig_maxOutOfOrderInSeconds = data.get("maxOutOfOrderInSeconds", 10)
        advanceConfig_offset = data.get("offset", "latest")
        advanceConfig_outputVars = data.get("outputVars", False)
        advanceConfig_persistOption = data.get("persistOption", True)
        advanceConfig_taskManagerMem = data.get("taskManagerMem", 2048)
        advanceConfig_contextField = data.get("contextField", "@rownumber")
        advanceConfig_contextFilterFields = data.get("contextFilterFields", "@path,@hostname")
        advanceConfig_derangementType = data.get("derangementType", None)  # 乱序数据处理方式
        advanceConfig_derangementTime = data.get("derangementTime", None)  # 定义乱序的时间

        # 聚合配置(实时任务前段界面找不到)
        aggregationConfig_enable = data.get("enable", True)
        aggregationConfig_windows = data.get("windows", 0)

        # 告警通知配置
        alertNoticeConfig_alertContent = data.get("alertContent",
                                                  "【${template_id}-${abnormal_name}】${source}聚类任务，【消息】${"
                                                  "start_time}，应用：${bs_name}，分组信息：${host_field_value}，${"
                                                  "agg_window}分钟内产生${value}条日志")
        alertNoticeConfig_emailEnable = data.get("emailEnable", False)
        alertNoticeConfig_emailTo = data.get("emailTo", [])
        alertNoticeConfig_emailSubject = data.get("emailSubject", "日志告警: ${source}")
        alertNoticeConfig_shellContent = data.get("shellContent", "")
        alertNoticeConfig_shellEnable = data.get("shellEnable", False)

        # 告警规则配置
        alertRuleConfig_advancedCompaction = data.get("advancedCompaction", False)
        alertRuleConfig_compactionCount = data.get("compactionCount", 2)
        alertRuleConfig_compactionMatchList = data.get("compactionMatchList", "")
        alertRuleConfig_compactionWindowSize = data.get("compactionWindowSize", 20)
        alertRuleConfig_warnCompactionType = data.get("warnCompactionType", "accumulate")  # 以上按数量压缩，20分钟内连续出现两个则告警

        # 关注模板
        attentionTemplates = data.get("attentionTemplates", [])

        # 聚类设置
        clusterConfig_format_rule = data.get("format_rule", "<content##[\s\S]*>")
        clusterConfig_replace_rule = data.get("replace_rule",
                                              [{'from': r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}', 'to': '$DateTime'},
                                               {'from': r'https?://[^\s]+', 'to': '$URL'},
                                               {'from': r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,5}', 'to': '$IPPort'},
                                               {'from': r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', 'to': '$IP'},
                                               {'from': r'(^|(?<=[^a-zA-Z\d\.]))\d+\.\d+(?=(\.?($|\s)|[^a-zA-Z\d\.]))',
                                                'to': '$NumFloat'}])
        clusterConfig_seperator_type = data.get("type", "RegExp")  # 定义分隔符类型，正则表达式
        clusterConfig_seperator_value = data.get("value", r"[^\w\u4e00-\u9fff\-/@]+")
        clusterConfig_keyword_type = data.get("type", "String")
        clusterConfig_keyword_value = data.get("value", "")
        clusterConfig_truncation = data.get("truncation", 100)
        clusterConfig_similarity = data.get("similarity", 0.5)
        clusterConfig_token_filter_ignore_digit = data.get("ignore_digit", False)
        clusterConfig_token_filter_ignore_replace_rule = data.get("ignore_replace_rule", False)

        # CMDB 配置
        cmdbInfo_serviceName = data.get("serviceName", "")
        cmdbInfo_serviceId = data.get("serviceId", "")
        cmdbInfo_field = data.get("field", "")
        cmdbInfo_type = data.get("type", "dynamic")

        # 数据源配置
        dataSource_fieldName = data.get("fieldName", "@message")
        dataSource_previewCount = data.get("previewCount", 0)
        dataSource_sourceId = data.get("sourceId", None)
        dataSource_timeField = data.get("timeField", "@timestamp")
        dataSource_timeFormat = data.get("timeFormat", "yyyy-MM-dd'T'HH:mm:ss.SSSZ")
        dataSource_timeType = data.get("timeType", "event")
        dataSource_timeZone = data.get("timeZone", "GMT+08:00")
        dataSource_type = data.get("type", "kafka")
        description = data.get("description", "this task created by auto test program")

        # 异常检测配置
        detectionConfig_enable = data.get("enable", True)
        detectionConfig_featureDetectionConfig_accidentalDays = data.get("accidentalDays", 7)
        detectionConfig_featureDetectionConfig_accidentalEnable = data.get("accidentalEnable", True)
        detectionConfig_featureDetectionConfig_accidentalThreshold = data.get("accidentalThreshold", 0.01)
        detectionConfig_featureDetectionConfig_guardEnable = data.get("guardEnable", False)
        detectionConfig_featureDetectionConfig_guardLogThreshold = data.get("guardLogThreshold", 10000)
        detectionConfig_featureDetectionConfig_guardMinute = data.get("guardMinute", 10)
        detectionConfig_featureDetectionConfig_startTime = data.get("startTime",
                                                                    datetime2timestamp(datetime.datetime.now()))
        detectionConfig_featureDetectionConfig_suddenDownEnable = data.get("suddenDownEnable", True)
        detectionConfig_featureDetectionConfig_suddenDownExtremumEnable = data.get("suddenDownExtremumEnable", True)
        detectionConfig_featureDetectionConfig_suddenDownFixedEnable = data.get("suddenDownFixedEnable", True)
        detectionConfig_featureDetectionConfig_suddenDownRateThreshold = data.get("suddenDownRateThreshold", 5)
        detectionConfig_featureDetectionConfig_suddenDownSensitivity = data.get("suddenDownSensitivity", 3)
        detectionConfig_featureDetectionConfig_suddenDownSmoothEnable = data.get("suddenDownSmoothEnable", True)
        detectionConfig_featureDetectionConfig_suddenDownTotalThreshold = data.get("suddenDownTotalThreshold", 10)
        detectionConfig_featureDetectionConfig_suddenDownWaveEnable = data.get("suddenDownWaveEnable", True)
        detectionConfig_featureDetectionConfig_suddenUpEnable = data.get("suddenUpEnable", True)
        detectionConfig_featureDetectionConfig_suddenUpExtremumEnable = data.get("suddenUpExtremumEnable", True)
        detectionConfig_featureDetectionConfig_suddenUpFixedEnable = data.get("suddenUpFixedEnable", True)
        detectionConfig_featureDetectionConfig_suddenUpRateThreshold = data.get("suddenUpRateThreshold", 95)
        detectionConfig_featureDetectionConfig_suddenUpSensitivity = data.get("suddenUpSensitivity", 3)
        detectionConfig_featureDetectionConfig_suddenUpSmoothEnable = data.get("suddenUpSmoothEnable", True)
        detectionConfig_featureDetectionConfig_suddenUpTotalThreshold = data.get("suddenUpTotalThreshold", 1000)
        detectionConfig_featureDetectionConfig_suddenUpWaveEnable = data.get("suddenUpWaveEnable", True)
        detectionConfig_featureDetectionConfig_type = data.get("type", "common")  # 异常检测模式：通用模式以及精细化模式
        detectionConfig_featureDetectionConfig_windows = data.get("windows", 5)
        detectionConfig_neverEnable = data.get("neverEnable", True)
        detectionConfig_noLogEnable = data.get("noLogEnable", True)
        detectionConfig_noLogStartTime = data.get("noLogStartTime", datetime2timestamp(datetime.datetime.now()))
        detectionConfig_noLogThreshold = data.get("noLogThreshold", 10)
        detectionConfig_novelDays = data.get("novelDays", 7)
        detectionConfig_novelDaysEnable = data.get("novelDaysEnable", True)
        detectionConfig_novelStartTime = data.get("novelStartTime", datetime2timestamp(datetime.datetime.now()))

        # 训练配置
        trainConfig_separate = data.get("separate", 1)  # 时间段分隔,单位为小时
        trainConfig_startTime = data.get("startTime", "00:30")
        trainConfig_strategy = data.get("strategy", "auto")
        trainConfig_cycle = data.get("cycle", "day")
        trainConfig_cycleNum = data.get("cycleNum", 2)
        trainConfig_dataInit = data.get("dataInit", False)
        trainConfig_taskType = data.get("taskType", "")
        trainConfig_dataSource = data.get("dataSource", None)

        # 请求体
        payload = {
            "advanceConfig": {
                "anomalyIndexShards": advanceConfig_anomalyIndexShards,
                "clusterMsgMaxLength": advanceConfig_clusterMsgMaxLength,
                "refreshInterval": advanceConfig_refreshInterval,
                "dsGroups": advanceConfig_dsGroups,
                "esIndexPattern": advanceConfig_esIndexPattern,
                "executorNumber": advanceConfig_executorNumber,
                "filter": advanceConfig_filter,
                "logIndexShards": advanceConfig_logIndexShards,
                "maxOutOfOrderInSeconds": advanceConfig_maxOutOfOrderInSeconds,
                "offset": advanceConfig_offset,
                "outputVars": advanceConfig_outputVars,
                "persistOption": advanceConfig_persistOption,
                "taskManagerMem": advanceConfig_taskManagerMem,
                "contextField": advanceConfig_contextField,
                "contextFilterFields": advanceConfig_contextFilterFields,
                "derangementType": advanceConfig_derangementType,
                "derangementTime": advanceConfig_derangementTime
            },
            "aggregationConfig": {
                "enable": aggregationConfig_enable,
                "windows": aggregationConfig_windows
            },
            "alertNoticeConfig": {
                "alertContent": alertNoticeConfig_alertContent,
                "emailEnable": alertNoticeConfig_emailEnable,
                "emailTo": alertNoticeConfig_emailTo,
                "emailSubject": alertNoticeConfig_emailSubject,
                "shellContent": alertNoticeConfig_shellContent,
                "shellEnable": alertNoticeConfig_shellEnable
            },
            "alertRuleConfig": {
                "advancedCompaction": alertRuleConfig_advancedCompaction,
                "compactionCount": alertRuleConfig_compactionCount,
                "compactionMatchList": alertRuleConfig_compactionMatchList,
                "compactionWindowSize": alertRuleConfig_compactionWindowSize,
                "warnCompactionType": alertRuleConfig_warnCompactionType
            },
            "attentionTemplates": attentionTemplates,
            "clusterConfig": {
                "format_rule": clusterConfig_format_rule,
                "replace_rule": clusterConfig_replace_rule,
                "seperator": {
                    "type": clusterConfig_seperator_type,
                    "value": clusterConfig_seperator_value
                },
                "keyword": {
                    "type": clusterConfig_keyword_type,
                    "value": clusterConfig_keyword_value
                },
                "truncation": clusterConfig_truncation,
                "similarity": clusterConfig_similarity,
                "token_filter": {
                    "ignore_digit": clusterConfig_token_filter_ignore_digit,
                    "ignore_replace_rule": clusterConfig_token_filter_ignore_replace_rule
                }
            },
            "cmdbInfo": {
                "serviceName": cmdbInfo_serviceName,
                "serviceId": cmdbInfo_serviceId,
                "field": cmdbInfo_field,
                "type": cmdbInfo_type
            },
            "dataSource": {
                "fieldName": dataSource_fieldName,
                "previewCount": dataSource_previewCount,
                "sourceId": dataSource_sourceId,
                "timeField": dataSource_timeField,
                "timeFormat": dataSource_timeFormat,
                "timeType": dataSource_timeType,
                "timeZone": dataSource_timeZone,
                "topic": dataSource_topic,
                "type": dataSource_type,
                "addressId": dataSource_addressId
            },
            "description": description,
            "detectionConfig": {
                "enable": detectionConfig_enable,
                "featureDetectionConfig": {
                    "accidentalDays": detectionConfig_featureDetectionConfig_accidentalDays,
                    "accidentalEnable": detectionConfig_featureDetectionConfig_accidentalEnable,
                    "accidentalThreshold": detectionConfig_featureDetectionConfig_accidentalThreshold,
                    "guardEnable": detectionConfig_featureDetectionConfig_guardEnable,
                    "guardLogThreshold": detectionConfig_featureDetectionConfig_guardLogThreshold,
                    "guardMinute": detectionConfig_featureDetectionConfig_guardMinute,
                    "startTime": detectionConfig_featureDetectionConfig_startTime,
                    "suddenDownEnable": detectionConfig_featureDetectionConfig_suddenDownEnable,
                    "suddenDownExtremumEnable": detectionConfig_featureDetectionConfig_suddenDownExtremumEnable,
                    "suddenDownFixedEnable": detectionConfig_featureDetectionConfig_suddenDownFixedEnable,
                    "suddenDownRateThreshold": detectionConfig_featureDetectionConfig_suddenDownRateThreshold,
                    "suddenDownSensitivity": detectionConfig_featureDetectionConfig_suddenDownSensitivity,
                    "suddenDownSmoothEnable": detectionConfig_featureDetectionConfig_suddenDownSmoothEnable,
                    "suddenDownTotalThreshold": detectionConfig_featureDetectionConfig_suddenDownTotalThreshold,
                    "suddenDownWaveEnable": detectionConfig_featureDetectionConfig_suddenDownWaveEnable,
                    "suddenUpEnable": detectionConfig_featureDetectionConfig_suddenUpEnable,
                    "suddenUpExtremumEnable": detectionConfig_featureDetectionConfig_suddenUpExtremumEnable,
                    "suddenUpFixedEnable": detectionConfig_featureDetectionConfig_suddenUpFixedEnable,
                    "suddenUpRateThreshold": detectionConfig_featureDetectionConfig_suddenUpRateThreshold,
                    "suddenUpSensitivity": detectionConfig_featureDetectionConfig_suddenUpSensitivity,
                    "suddenUpSmoothEnable": detectionConfig_featureDetectionConfig_suddenUpSmoothEnable,
                    "suddenUpTotalThreshold": detectionConfig_featureDetectionConfig_suddenUpTotalThreshold,
                    "suddenUpWaveEnable": detectionConfig_featureDetectionConfig_suddenUpWaveEnable,
                    "type": detectionConfig_featureDetectionConfig_type,
                    "windows": detectionConfig_featureDetectionConfig_windows
                },
                "neverEnable": detectionConfig_neverEnable,
                "noLogEnable": detectionConfig_noLogEnable,
                "noLogStartTime": detectionConfig_noLogStartTime,
                "noLogThreshold": detectionConfig_noLogThreshold,
                "novelDays": detectionConfig_novelDays,
                "novelDaysEnable": detectionConfig_novelDaysEnable,
                "novelStartTime": detectionConfig_novelStartTime
            },
            "name": name,
            "trainConfig": {
                "separate": trainConfig_separate,
                "startTime": trainConfig_startTime,
                "strategy": trainConfig_strategy,
                "cycle": trainConfig_cycle,
                "cycleNum": trainConfig_cycleNum,
                "dataInit": trainConfig_dataInit,
                "taskType": trainConfig_taskType,
                "dataSource": trainConfig_dataSource
            }
        }

        print(payload)


if __name__ == '__main__':
    unittest.main()
