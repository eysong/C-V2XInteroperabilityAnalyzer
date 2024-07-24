import pandas as pd

# Eval methods: 
# 0 = compare with max, min (val1, val2)
# 1 = octet count (val1, 00)
# 2 = bit string (val1, 00)
# 3 = boolean (00, 00)
# 4 = hashalg list (00, 00)

saej2735_bsm_ref = [    # col[0] = field name, col[1] = parent name, col[2] = length, col[3] = eval method, col[4] = ref value 1, col[5] = ref value 2, col[6] = mandatory?
    ["j2735_2016.msgCnt", "j2735_2016.coreData_element", 1, 0, 0, 127, True],  # start of coreData (mandatory)
    ["j2735_2016.id", "j2735_2016.coreData_element", 4, 1, 4, 00, True],
    ["j2735_2016.secMark", "j2735_2016.coreData_element", 2, 0, 0, 65535, True],
    ["j2735_2016.lat", "j2735_2016.coreData_element", 4, 0, -900000000, 900000001, True],
    ["j2735_2016.long", "j2735_2016.coreData_element", 4, 0, -1799999999, 1800000001, True],
    ["j2735_2016.elev", "j2735_2016.coreData_element", 2, 0, -4096, 61439, True],
    ["j2735_2016.semiMajor", "j2735_2016.accuracy_element", 1, 0, 0, 255, True],
    ["j2735_2016.semiMinor", "j2735_2016.accuracy_element", 1, 0, 0, 255, True],
    ["j2735_2016.orientation", "j2735_2016.accuracy_element", 2, 0, 0, 65535, True],
    ["j2735_2016.transmission", "j2735_2016.coreData_element", 1, 0, 0, 7, True],
    ["j2735_2016.speed", "j2735_2016.coreData_element", 2, 0, 0, 8191, True],
    ["j2735_2016.heading", "j2735_2016.coreData_element", 2, 0, 0, 28800, True],
    ["j2735_2016.angle", "j2735_2016.coreData_element", 1, 0, -126, 127, True],
    ["j2735_2016.long", "j2735_2016.accelSet_element", 2, 0, -2000, 2001, True],
    ["j2735_2016.lat", "j2735_2016.accelSet_element", 2, 0, -2000, 2001, True],
    ["j2735_2016.vert", "j2735_2016.accelSet_element", 1, 0, -127, 127, True],
    ["j2735_2016.yaw", "j2735_2016.accelSet_element", 2, 0, -32767, 32767, True],
    ["j2735_2016.wheelBrakes", "j2735_2016.brakes_element", 1, 2, 5, 00, True],
    ["j2735_2016.traction", "j2735_2016.brakes_element", 1, 0, 0, 3, True],
    ["j2735_2016.abs", "j2735_2016.brakes_element", 1, 0, 0, 3, True],
    ["j2735_2016.scs", "j2735_2016.brakes_element", 1, 0, 0, 3, True],
    ["j2735_2016.brakeBoost", "j2735_2016.brakes_element", 1, 0, 0, 2, True],
    ["j2735_2016.auxBrakes", "j2735_2016.brakes_element", 1, 0, 0, 2, True],
    ["j2735_2016.width", "j2735_2016.size_element", 2, 0, 0, 1023, True],
    ["j2735_2016.length", "j2735_2016.size_element", 2, 0, 0, 4095, True],
    ["j2735_2016.partII.Id", "j2735_2016.PartIIcontent_element", 1, 0, 0, 63, False],  # start of partII (optional)
    ["j2735_2016.events", "j2735_2016.PartII_Value_element", 2, 2, 13, 00, False],
    ["j2735_2016.year", "j2735_2016.utcTime_element", 2, 0, 0, 4095, False],
    ["j2735_2016.month", "j2735_2016.utcTime_element", 1, 0, 0, 12, False],
    ["j2735_2016.day", "j2735_2016.utcTime_element", 1, 0, 0, 31, False],
    ["j2735_2016.hour", "j2735_2016.utcTime_element", 1, 0, 0, 31, False],
    ["j2735_2016.minute", "j2735_2016.utcTime_element", 1, 0, 0, 60, False],
    ["j2735_2016.second", "j2735_2016.utcTime_element", 2, 0, 0, 65535, False],
    ["j2735_2016.offset", "j2735_2016.utcTime_element", 2, 0, -840, 840, False],
    ["j2735_2016.long", "j2735_2016.initialPosition_element", 4, 0, -1799999999, 1800000001, False],
    ["j2735_2016.lat", "j2735_2016.initialPosition_element", 4, 0, -900000000, 900000001, False],
    ["j2735_2016.elevation", "j2735_2016.initialPosition_element", 2, 0, -4096, 61439, False],
    ["j2735_2016.heading", "j2735_2016.initialPosition_element", 2, 0, 0, 28800, False],
    ["j2735_2016.transmission", "j2735_2016.TransmissionAndSpeed_element", 1, 0, 0, 7, False],
    ["j2735_2016.speed", "j2735_2016.TransmissionAndSpeed_element", 2, 0, 0, 8191, False],
    ["j2735_2016.semiMajor", "j2735_2016.posAccuracy_element", 1, 0, 0, 255, False],
    ["j2735_2016.semiMinor", "j2735_2016.posAccuracy_element", 1, 0, 0, 255, False],
    ["j2735_2016.orientation", "j2735_2016.posAccuracy_element", 2, 0, 0, 65535, False],
    ["j2735_2016.timeConfidence", "j2735_2016.initialPosition_element", 1, 0, 0, 39, False],
    ["j2735_2016.pos", "j2735_2016.posConfidence_element", 1, 0, 0, 15, False],
    ["j2735_2016.elevation", "j2735_2016.posConfidence_element", 1, 0, 0, 15, False],
    ["j2735_2016.heading", "j2735_2016.speedConfidence_element", 1, 0, 0, 7, False],
    ["j2735_2016.speed", "j2735_2016.speedConfidence_element", 1, 0, 0, 7, False],
    ["j2735_2016.throttle", "j2735_2016.speedConfidence_element", 1, 0, 0, 3, False],
    ["j2735_2016.radiusOfCurve", "j2735_2016.pathPrediction_element", 2, 0, -32767, 32767, False],
    ["j2735_2016.confidence", "j2735_2016.pathPrediction_element", 1, 0, 0, 200, False],
    ["j2735_2016.lights", "j2735_2016.PartII_Value_element", 2, 3, 9, 00, False],
    ["j2735_2016.sspRights", "j2735_2016.vehicleAlerts_element", 1, 0, 0, 31, False],
    ["j2735_2016.sirenUse", "j2735_2016.vehicleAlerts_element", 1, 0, 0, 3, False],
    ["j2735_2016.lightsUse", "j2735_2016.vehicleAlerts_element", 1, 0, 0, 63, False],
    ["j2735_2016.multi", "j2735_2016.vehicleAlerts_element", 1, 0, 0, 3, False],
    ["j2735_2016.sspRights", "j2735_2016.events_element", 1, 0, 0, 31, False],
    ["j2735_2016.event", "j2735_2016.events_element", 2, 2, 16, 00, False],
    ["j2735_2016.responseType", "j2735_2016.vehicleAlerts_element", 1, 0, 0, 6, False],
    ["j2735_2016.typeEvent", "j2735_2016.description_element", 2, 0, 0, 65535, False],
    ["j2735_2016.priority", "j2735_2016.description_element", 1, 1, 1, 00, False],
    ["j2735_2016.heading", "j2735_2016.description_element", 2, 2, 16, 00, False],
    ["j2735_2016.extent", "j2735_2016.description_element", 1, 0, 0, 15, False],
    ["j2735_2016.sspRights", "j2735_2016.trailers_element", 1, 0, 0, 31, False],
    ["j2735_2016.pivotOffset", "j2735_2016.connection_element", 1, 0, -1024, 1023, False],
    ["j2735_2016.pivotAngle", "j2735_2016.connection_element", 2, 0, 0, 28800, False],
    ["j2735_2016.pivots", "j2735_2016.connection_element", 1, 3, 0, 00, False],
    ["j2735_2016.classification", "j2735_2016.PartII_Value_element", 1, 0, 0, 255, False],
    ["j2735_2016.keyType", "j2735_2016.classDetails_element", 1, 0, 0, 255, False],
    ["j2735_2016.role", "j2735_2016.classDetails_element", 1, 0, 0, 22, False],
    ["j2735_2016.iso3883", "j2735_2016.classDetails_element", 1, 0, 0, 100, False],
    ["j2735_2016.hpmsType", "j2735_2016.classDetails_element", 1, 0, 0, 15, False],
    ["j2735_2016.vehicleType", "j2735_2016.classDetails_element", 1, 0, 0, 15, False],
    ["j2735_2016.responseEquip", "j2735_2016.classDetails_element", 2, 9985, 10113, False],
    ["j2735_2016.responderType", "j2735_2016.classDetails_element", 2, 9729, 9742, False],
    ["j2735_2016.fuelType", "j2735_2016.classDetails_element", 1, 0, 0, 15, False],
    ["j2735_2016.height", "j2735_2016.vehicleData_element", 1, 0, 0, 127, False],
    ["j2735_2016.front", "j2735_2016.bumpers_element", 1, 0, 0, 127, False],
    ["j2735_2016.rear", "j2735_2016.bumpers_element", 1, 0, 0, 127, False],
    ["j2735_2016.mass", "j2735_2016.vehicleData_element", 1, 0, 0, 255, False],
    ["j2735_2016.trailerWeight", "j2735_2016.vehicleData_element", 2, 0, 0, 64255, False],
    ["j2735_2016.front", "j2735_2016.bumpers_element", 1, 0, 0, 127, False],
    ["j2735_2016.isRaining", "j2735_2016.weatherReport_element", 1, 1, 3, False],
    ["j2735_2016.rainRate", "j2735_2016.weatherReport_element", 2, 0, 0, 65535, False],
    ["j2735_2016.precipSituation", "j2735_2016.weatherReport_element", 1, 1, 15, False],
    ["j2735_2016.solarRadiation", "j2735_2016.weatherReport_element", 2, 0, 0, 65535, False],
    ["j2735_2016.friction", "j2735_2016.weatherReport_element", 1, 0, 0, 101, False],
    ["j2735_2016.roadFriction", "j2735_2016.weatherReport_element", 1, 0, 0, 50, False],
    ["j2735_2016.airTemp", "j2735_2016.weatherProbe_element", 1, 0, 0, 191, False],
    ["j2735_2016.airPressure", "j2735_2016.weatherProbe_element", 1, 0, 0, 255, False],
    ["j2735_2016.statusFront", "j2735_2016.rainRates_element", 1, 0, 0, 6, False],
    ["j2735_2016.rateFront", "j2735_2016.rainRates_element", 1, 0, 0, 127, False],
    ["j2735_2016.statusRear", "j2735_2016.rainRates_element", 1, 0, 0, 6, False],
    ["j2735_2016.rateRear", "j2735_2016.rainRates_element", 1, 0, 0, 127, False],
    ["j2735_2016.obDist", "j2735_2016.obstacle_element", 1, 0, 0, 32767, False],
    ["j2735_2016.obDist", "j2735_2016.obstacle_element", 1, 0, 0, 28800, False],
    ["j2735_2016.year", "j2735_2016.dateTime_element", 2, 0, 0, 4095, False],
    ["j2735_2016.month", "j2735_2016.dateTime_element", 1, 0, 0, 12, False],
    ["j2735_2016.day", "j2735_2016.dateTime_element", 1, 0, 0, 31, False],
    ["j2735_2016.hour", "j2735_2016.dateTime_element", 1, 0, 0, 31, False],
    ["j2735_2016.minute", "j2735_2016.dateTime_element", 1, 0, 0, 60, False],
    ["j2735_2016.second", "j2735_2016.dateTime_element", 2, 0, 0, 65535, False],
    ["j2735_2016.offset", "j2735_2016.dateTime_element", 2, 0, -840, 840, False],
    ["j2735_2016.vertEvent", "j2735_2016.obstacle_element", 1, 2, 5, 00, False],
    ]
saej2735_bsm_refdf = pd.DataFrame(saej2735_bsm_ref, columns = ["field", "parent", "length", "eval method", "val1", "val2", "mandatory"])

saej2735_spat_ref = [
    ["j2735_2016.timeStamp", "j2735_2016.value_element", 2, 0, 0, 527040, False],
    ["j2735_2016.region", "j2735_2016.id_element", 2, 0, 0, 65535, False],
    ["j2735_2016.id", "j2735_2016.id_element", 2, 0, 0, 65535, True],
    ["j2735_2016.revision", "j2735_2016.IntersectionState_element", 1, 0, 0, 127, True],
    ["j2735_2016.status", "j2735_2016.IntersectionState_element", 2, 2, 16, 00, True],
    ["j2735_2016.moy", "j2735_2016.IntersectionState_element", 2, 0, 0, 527040, False],
    ["j2735_2016.timeStamp", "j2735_2016.IntersectionState_element", 2, 0, 0, 65535, False],
    ["j2735_2016.laneID", "j2735_2016.IntersectionState_element", 2, 0, 0, 255, False],
    ["j2735_2016.signalGroup", "j2735_2016.MovementState_element", 1, 0, 0, 255, True],
    ["j2735_2016.eventState", "j2735_2016.MovementEvent_element", 1, 0, 0, 9, True],
    ["j2735_2016.startTime", "j2735_2016.timing_element", 2, 0, 0, 36001, False],
    ["j2735_2016.minEndTime", "j2735_2016.timing_element", 2, 0, 0, 36001, False],
    ["j2735_2016.maxEndTime", "j2735_2016.timing_element", 2, 0, 0, 36001, False],
    ["j2735_2016.likelyTime", "j2735_2016.timing_element", 2, 0, 0, 36001, False],
    ["j2735_2016.confidence", "j2735_2016.timing_element", 2, 0, 0, 15, False],
    ["j2735_2016.nextTime", "j2735_2016.timing_element", 2, 0, 0, 36001, False],
    ["j2735_2016.type", "j2735_2016.AdvisorySpeed_element", 1, 0, 0, 3, False],
    ["j2735_2016.speed", "j2735_2016.AdvisorySpeed_element", 2, 0, 0, 500, False], # double length problem
    ["j2735_2016.confidence", "j2735_2016.AdvisorySpeed_element", 2, 0, 0, 7, False],
    ["j2735_2016.distance", "j2735_2016.AdvisorySpeed_element", 2, 0, 0, 10000, False], # double length problem
    ["j2735_2016.class", "j2735_2016.AdvisorySpeed_element", 2, 0, 0, 255, False],
    ["j2735_2016.connectionID", "j2735_2016.ConnectionManeuverAssist_element", 2, 0, 0, 10000, False],
    ["j2735_2016.queueLength", "j2735_2016.ConnectionManeuverAssist_element", 2, 0, 0, 10000, False],
    ["j2735_2016.availableStorageLength", "j2735_2016.ConnectionManeuverAssist_element", 2, 0, 0, 10000, False],
    ["j2735_2016.waitOnStop", "j2735_2016.ConnectionManeuverAssist_element", 1, 3, 00, 00, False],
    ["j2735_2016.pedBicycleDetect", "j2735_2016.ConnectionManeuverAssist_element", 1, 3, 00, 00, False],
]
saej2735_spat_refdf = pd.DataFrame(saej2735_spat_ref, columns = ["field", "parent", "length", "eval method", "val1", "val2", "mandatory"])

saej2735_rsa_ref = [
    ["j2735_2016.msgCnt", "j2735_2016.value_element", 1, 0, 0, 127, True],
    ["j2735_2016.timeStamp", "j2735_2016.value_element", 3, 0, 0, 527040, False],
    ["j2735_2016.typeEvent", "j2735_2016.value_element", 2, 0, 0, 65535, True],
    ["j2735_2016.priority", "j2735_2016.value_element", 1, 1, 1, 00, False],
    ["j2735_2016.extent", "j2735_2016.value_element", 1, 0, 0, 15, False],
    ["j2735_2016.year", "j2735_2016.utcTime", 2, 0, 0, 4095, False],
    ["j2735_2016.month", "j2735_2016.utcTime", 1, 0, 0, 12, False],
    ["j2735_2016.day", "j2735_2016.utcTime", 1, 0, 0, 31, False],
    ["j2735_2016.hour", "j2735_2016.utcTime", 1, 0, 0, 31, False],
    ["j2735_2016.long", "j2735_2016.position_element", 4, 0, -1799999999, 1800000001, False],
    ["j2735_2016.lat", "j2735_2016.position_element", 4, 0, -900000000, 900000001, False],
    ["j2735_2016.elevation", "j2735_2016.position_element", 2, 0, -4096, 61439, False],
    ["j2735_2016.heading", "j2735_2016.position_element", 2, 0, 0, 28800, False],
    ["j2735_2016.transmission", "j2735_2016.speed_element", 1, 0, 0, 7, False],
    ["j2735_2016.speed", "j2735_2016.speed_element", 1, 0, 0, 8191, False],
    ["j2735_2016.semiMajor", "j2735_2016.posAccuracy_element", 1, 0, 0, 255, False],
    ["j2735_2016.semiMinor", "j2735_2016.posAccuracy_element", 1, 0, 0, 255, False],
    ["j2735_2016.orientation", "j2735_2016.posAccuracy_element", 2, 0, 0, 65535, False],
    ["j2735_2016.timeConfidence", "j2735_2016.position_element", 1, 0, 0, 39, False],
    ["j2735_2016.pos", "j2735_2016.posConfidence_element", 1, 0, 0, 15, False],
    ["j2735_2016.elevation", "j2735_2016.posConfidence_element", 1, 0, 0, 15, False],
    ["j2735_2016.heading", "j2735_2016.speedConfidence_element", 1, 0, 0, 7, False],
    ["j2735_2016.speed", "j2735_2016.speedConfidence_element", 1, 0, 0, 7, False],
    ["j2735_2016.throttle", "j2735_2016.speedConfidence_element", 1, 0, 0, 3, False],
    ["j2735_2016.furtherInfoID", "j2735_2016.value_element", 2, 1, 2, 00, False],
]
saej2735_rsa_refdf = pd.DataFrame(saej2735_rsa_ref, columns = ["field", "parent", "length", "eval method", "val1", "val2", "mandatory"])

saej2735_tim_ref = [
    ["j2735_2016.msgCnt", "j2735_2016.value_element", 1, 0, 0, 127, True],
    ["j2735_2016.timeStamp", "j2735_2016.value_element", 2, 0, 0, 527040, False],
    ["j2735_2016.packetID", "j2735_2016.value_element", 9, 1, 9, 00, False],
    ["j2735_2016.sspTimRights", "j2735_2016.TravelerDataFrame_element", 1, 0, 0, 31, True],
    ["j2735_2016.frameType", "j2735_2016.TravelerDataFrame_element", 1, 0, 0, 3, True],
    ["j2735_2016.lat", "j2735_2016.position_element", 4, 0, -900000000, 900000001, True],
    ["j2735_2016.long", "j2735_2016.position_element", 4, 0, -1799999999, 1800000001, True],
    ["j2735_2016.elevation", "j2735_2016.position_element", 2, 0, -4096, 61439, False],
    ["j2735_2016.viewAngle", "j2735_2016.roadSignID_element", 2, 2, 16, 00, True],
    ["j2735_2016.mutcdCode", "j2735_2016.roadSignID_element", 1, 0, 0, 6, False],
    ["j2735_2016.crc", "j2735_2016.roadSignID_element", 2, 1, 2, 00, False],
    ["j2735_2016.startYear", "j2735_2016.TravelerDataFrame_element", 2, 0, 0, 4095, False],
    ["j2735_2016.startTime", "j2735_2016.TravelerDataFrame_element", 3, 0, 0, 527040, True],
    ["j2735_2016.durationTime", "j2735_2016.TravelerDataFrame_element", 2, 0, 0, 32000, False], # problem, should be mandatory
    ["j2735_2016.priority", "j2735_2016.TravelerDataFrame_element", 1, 0, 0, 7, True],
    ["j2735_2016.sspLocationRights", "j2735_2016.TravelerDataFrame_element", 1, 0, 0, 31, True],
    ["j2735_2016.region", "j2735_2016.id_element", 2, 0, 0, 65535, False],
    ["j2735_2016.id", "j2735_2016.id_element", 2, 0, 0, 65535, False],
    ["j2735_2016.lat", "j2735_2016.anchor_element", 4, 0, -900000000, 900000001, False],
    ["j2735_2016.long", "j2735_2016.anchor_element", 4, 0, -1799999999, 1800000001, False],
    ["j2735_2016.elevation", "j2735_2016.anchor_element", 2, 0, -4096, 61439, False],
    ["j2735_2016.laneWidth", "j2735_2016.GeographicalPath_element", 2, 0, 0, 32767, False],
    ["j2735_2016.directionality", "j2735_2016.GeographicalPath_element", 1, 0, 0, 3, False],
    ["j2735_2016.closedPath", "j2735_2016.GeographicalPath_element", 1, 3, 00, 00, False],
    ["j2735_2016.direction", "j2735_2016.GeographicalPath_element", 2, 2, 16, 00, False],
    ["j2735_2016.scale", "j2735_2016.path_element", 2, 0, 0, 15, False],
    ["j2735_2016.x", "j2735_2016.node_XY6_element", 2, 0, -32768, 32767, False],
    ["j2735_2016.y", "j2735_2016.node_XY6_element", 2, 0, -32768, 32767, False],
    ["j2735_2016.NodeAttributeXY", "j2735_2016.localNode_element", 2, 0, 0, 11, False],
    ["j2735_2016.SegmentAttributeXY", "j2735_2016.disabled", 2, 0, 0, 37, False],
    ["j2735_2016.SegmentAttributeXY", "j2735_2016.enabled", 2, 0, 0, 37, False],
    ["j2735_2016.dWidth", "j2735_2016.attributes_element", 2, 0, -512, 511, False],
    ["j2735_2016.dElevation", "j2735_2016.attributes_element", 2, 0, -512, 511, False],
    ["j2735_2016.dWidth", "j2735_2016.attributes_element", 2, 0, -512, 511, False],
    ["j2735_2016.sspMsgRights1", "j2735_2016.TravelerDataFrame_element", 1, 0, 0, 31, True],
    ["j2735_2016.sspMsgRights2", "j2735_2016.TravelerDataFrame_element", 1, 0, 0, 31, True],
]
saej2735_tim_refdf = pd.DataFrame(saej2735_tim_ref, columns = ["field", "parent", "length", "eval method", "val1", "val2", "mandatory"])

saej2735_map_ref = [
    ["j2735_2016.timeStamp", "j2735_2016.value_element", 3, 0, 0, 527040, False],
    ["j2735_2016.msgIssueRevision", "j2735_2016.value_element", 1, 0, 0, 127, True],
    ["j2735_2016.layerType", "j2735_2016.value_element", 1, 0, 0, 7, False],
    ["j2735_2016.layerID", "j2735_2016.value_element", 1, 0, 0, 100, False],
    ["j2735_2016.region", "j2735_2016.id_element", 2, 0, 0, 65535, False],
    ["j2735_2016.id", "j2735_2016.id_element", 2, 0, 0, 65535, False],
    ["j2735_2016.revision", "j2735_2016.IntersectionGeometry_element", 1, 0, 0, 127, True],
    ["j2735_2016.lat", "j2735_2016.refPoint_element", 4, 0, -900000000, 900000001, True],
    ["j2735_2016.long", "j2735_2016.refPoint_element", 4, 0, -1799999999, 1800000001, True],
    ["j2735_2016.elevation", "j2735_2016.refPoint_element", 2, 0, -4096, 61439, False],
    ["j2735_2016.laneWidth", "j2735_2016.IntersectionGeometry_element", 2, 0, 0, 32767, False],
    ["j2735_2016.type", "j2735_2016.RegulatorySpeedLimit_element", 1, 0, 0, 12, False],
    ["j2735_2016.speed", "j2735_2016.RegulatorySpeedLimit_element", 2, 0, 0, 8191, False],
    ["j2735_2016.laneID", "j2735_2016.GenericLane_element", 1, 0, 0, 255, True],
    ["j2735_2016.ingressApproach", "j2735_2016.GenericLane_element", 1, 0, 0, 15, False],
    ["j2735_2016.egressApproach", "j2735_2016.GenericLane_element", 1, 0, 0, 15, False],
    ["j2735_2016.directionalUse", "j2735_2016.laneAttributes_element", 1, 2, 2, 0, True],
    ["j2735_2016.sharedWith", "j2735_2016.laneAttributes_element", 2, 2, 10, 0, True],
    ["j2735_2016.laneType", "j2735_2016.laneAttributes_element", 4, 0, 0, 7, True],
    ["j2735_2016.vehicle", "j2735_2016.laneType", 2, 2, 16, 00, False],
    ["j2735_2016.crosswalk", "j2735_2016.laneType", 2, 2, 16, 00, False],
    ["j2735_2016.bikeLane", "j2735_2016.laneType", 2, 2, 16, 00, False],
    ["j2735_2016.sidewalk", "j2735_2016.laneType", 2, 2, 16, 00, False],
    ["j2735_2016.median", "j2735_2016.laneType", 2, 2, 16, 00, False],
    ["j2735_2016.striping", "j2735_2016.laneType", 2, 2, 16, 00, False],
    ["j2735_2016.trackedVehicle", "j2735_2016.laneType", 2, 2, 16, 00, False],
    ["j2735_2016.parking", "j2735_2016.laneType", 2, 2, 16, 00, False],
    ["j2735_2016.maneuvers", "j2735_2016.GenericLane_element", 2, 2, 12, 00, False],
    ["j2735_2016.x", "j2735_2016.node_XY6_element", 2, 0, -32768, 32767, True],
    ["j2735_2016.y", "j2735_2016.node_XY6_element", 2, 0, -32768, 32767, True],
    ["j2735_2016.NodeAttributeXY", "j2735_2016.localNode_element", 1, 0, 0, 11, False],
    ["j2735_2016.SegmentAttributeXY", "j2735_2016.enabled_element", 1, 0, 0, 37, False],
    ["j2735_2016.SegmentAttributeXY", "j2735_2016.disabled_element", 1, 0, 0, 37, False],
    ["j2735_2016.pathEndPointAngle", "j2735_2016.LaneDataAttribute_element", 1, 0, -150, 150, False],
    ["j2735_2016.laneCrownPointCenter", "j2735_2016.LaneDataAttribute_element", 1, 0, -128, 127, False],
    ["j2735_2016.laneCrownPointLeft", "j2735_2016.LaneDataAttribute_element", 1, 0, -128, 127, False],
    ["j2735_2016.laneCrownPointRight", "j2735_2016.LaneDataAttribute_element", 1, 0, -128, 127, False],
    ["j2735_2016.laneAngle", "j2735_2016.LaneDataAttribute_element", 1, 0, -180, 180, False],
    ["j2735_2016.type", "j2735_2016.RegulatorySpeedLimit_element", 1, 0, 0, 12, False],
    ["j2735_2016.speed", "j2735_2016.RegulatorySpeedLimit_element", 2, 0, 0, 8191, False],
    ["j2735_2016.dWidth", "j2735_2016.attributes_element", 2, 0, -512, 511, False],
    ["j2735_2016.dElevation", "j2735_2016.attributes_element", 2, 0, -512, 511, False],
    ["j2735_2016.lane", "j2735_2016.connectingLane_element", 1, 0, 0, 255, False],
    ["j2735_2016.maneuver", "j2735_2016.connectingLane_element", 2, 2, 12, 0, False],
    ["j2735_2016.region", "j2735_2016.remoteIntersection_element", 2, 0, 0, 65535, False],
    ["j2735_2016.id", "j2735_2016.remoteIntersection_element", 2, 0, 0, 65535, False],
    ["j2735_2016.signalGroup", "j2735_2016.Connection_element", 1, 0, 0, 255, False],
    ["j2735_2016.userClass", "j2735_2016.Connection_element", 1, 0, 0, 255, False],
    ["j2735_2016.connectionID", "j2735_2016.Connection_element", 1, 0, 0, 255, False],
    ["j2735_2016.LaneID", "j2735_2016.overlays_element", 1, 0, 0, 255, False]
]
saej2735_map_refdf = pd.DataFrame(saej2735_map_ref, columns = ["field", "parent", "length", "eval method", "val1", "val2", "mandatory"]) 