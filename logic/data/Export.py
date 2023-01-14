import re

from logic.Base import BaseLogic
from common.convert import class2json
import xlwt
import xlrd


class DataExportLogic():
    # 按照模板导出评价方案
    def export_all_bm_score(self, teacher_name: str, dept: str, actyear: str, schemeid: str):
        query = {}
        if actyear is not None and len(actyear) > 0:
            query['actyear'] = actyear
        if teacher_name is not None and len(teacher_name) > 0:
            import re
            query['jsxm'] = re.compile(teacher_name)
        if schemeid is not None and len(schemeid) > 0:
            query['schemeid'] = str(schemeid)
        if dept is not None and len(dept) > 0:
            query['kkxy'] = dept
        from logic.score.Score import ScoreLogic
        sl = ScoreLogic()
        result, num, msg = sl.search_no_page(query=query)
        scores = result
        from logic.course_evaluate.CourseEvaluate import CourseEvaluateLogic
        cel = CourseEvaluateLogic()
        result, num, msg = cel.get_all_fromdb()
        import xlwt
        workbook = xlwt.Workbook(encoding='utf-8')
        if schemeid is not None and len(schemeid) > 0:
            workbook = self.export_score_to_excel(scores, schemeid, workbook)
        else:
            for ce in result:
                ss = [];
                for s in scores:
                    if str(s["schemeid"]) == str(ce["_id"]):
                        ss.append(s)
                workbook = self.export_score_to_excel(ss, str(ce["_id"]), workbook)
        return workbook

    def export_scores_by_query(self, bm: str, actyear: str, ):
        from logic.course_evaluate.CourseEvaluate import CourseEvaluateLogic
        cel = CourseEvaluateLogic()
        result, num, msg = cel.get_all_fromdb()
        import xlwt
        workbook = xlwt.Workbook(encoding='utf-8')
        for ce in result:
            workbook = self.export_bm_score_by_schemeid(str(ce["_id"]), bm, actyear, workbook)
        return workbook

    def export_score_to_excel(self, scores: list, schemeid: str, workbook=None):
        from enviroment import project_dir
        import os
        fullfilename = project_dir + os.sep + "template" + os.sep + "exportscore_template.xlsx"
        if not os.path.exists(fullfilename):
            raise Exception("模板文件不存在")
        # print(fullfilename)
        wb = xlrd.open_workbook(fullfilename)
        sh = wb.sheet_by_index(0)
        columns = sh.row_values(0)
        from logic.course_evaluate.CourseEvaluate import CourseEvaluateLogic
        cel = CourseEvaluateLogic()
        result, num, msg = cel.get_ce_fis_sis(schemeid=schemeid)
        scheme = result
        if scheme is None:
            raise Exception("评价指标id错误")
        # print(class2json(result))
        # print(num)
        from logic.score.Score import ScoreLogic
        sl = ScoreLogic()
        # 创建一个workbook 设置编码
        if workbook is None:
            workbook = xlwt.Workbook(encoding='utf-8')
        # 创建一个worksheet
        worksheet = workbook.add_sheet(scheme["name"])
        # 写入excel
        # 参数对应 行, 列, 值
        if "name" in scheme:
            # worksheet.write(0, 0, label=scheme["name"])
            pass
        for index, column in enumerate(columns):
            worksheet.write(0, index, label=str(column).strip())
        columnnum = len(columns)
        if "first_index" in scheme:
            fis: list = scheme["first_index"]
            for index, fi in enumerate(fis):
                worksheet.write(0, columnnum + index * 4, label=str(fi["name"]).strip())
                worksheet.write(0, columnnum + index * 4 + 1, label=str(fi["name"]).strip() + "所占比例")
                worksheet.write(0, columnnum + index * 4 + 2, label=str(fi["name"]).strip() + "等价分数")
                worksheet.write(0, columnnum + index * 4 + 3, label=str(fi["name"]).strip() + "得分")
        if len(scores) > 0:
            tags = sh.row_values(1)
            for score_num, score in enumerate(scores):
                # score: dict = scores[0]
                # print(score)
                for index, tag in enumerate(tags):
                    replace_tag = str(tag).strip().replace("'", "").replace('<$', "").replace('>', '')
                    if replace_tag.lower() == "score_user_info.name":
                        worksheet.write(score_num + 1, index, label=str(score["score_user_info"]["name"]).strip())
                    elif replace_tag.lower() == "scheme_name":
                        worksheet.write(score_num + 1, index, label=str(scheme["name"]).strip())
                    else:
                        zz = r'<.*?>'
                        if replace_tag in score:
                            # print(replace_tag, ":", score[replace_tag])
                            worksheet.write(score_num + 1, index,
                                            label=str(re.sub(zz, "", str(score[replace_tag]))).strip())
                        else:
                            worksheet.write(score_num + 1, index, label=str(re.sub(zz, "", str(tag))).strip())
                # print("result" in score) and (len(score["result"]) > 0)
                if ("result" in score) and (len(score["result"]) > 0):
                    for index2, fi in enumerate(fis):
                        for r in score["result"]:
                            # print("fi" in r and "_id" in fi)
                            if "fi" in r and "_id" in fi:
                                result_fi_id = r["fi"]["id"]
                                # print(str(result_fi_id).strip() == str(fi["_id"]).strip())
                                if str(result_fi_id).strip() == str(fi["_id"]).strip():
                                    if "name" in r["si"]:
                                        worksheet.write(score_num + 1, columnnum + index2 * 4,
                                                        label=str(r["si"]["name"]).strip())
                                    elif len(r["si"]) > 0 and "name" in r["si"][0]:
                                        worksheet.write(score_num + 1, columnnum + index2 * 4,
                                                        label=str(r["si"][0]["name"]).strip())
                                    if "proportion" in r["fi"]:
                                        worksheet.write(score_num + 1, columnnum + index2 * 4 + 1,
                                                        label=str(r["fi"]["proportion"]).strip() + "%")
                                    if "value" in r["si"]:
                                        worksheet.write(score_num + 1, columnnum + index2 * 4 + 2,
                                                        label=str(r["si"]["value"]))
                                    elif len(r["si"]) > 0 and "value" in r["si"][0]:
                                        worksheet.write(score_num + 1, columnnum + index2 * 4 + 2,
                                                        label=str(r["si"][0]["value"]))
                                    if "value" in r["si"] and "proportion" in r["fi"]:
                                        worksheet.write(score_num + 1, columnnum + index2 * 4 + 3,
                                                        label=int(str(r["fi"]["proportion"])) * int(
                                                            str(r["si"]["value"])) / 100)
                                    elif len(r["si"]) > 0 and "value" in r["si"][0] and "proportion" in r["fi"]:
                                        worksheet.write(score_num + 1, columnnum + index2 * 4 + 3,
                                                        label=int(str(r["fi"]["proportion"])) * int(str(
                                                            r["si"][0]["value"])) / 100)

        return workbook

    def export_bm_score_by_schemeid(self, schemeid: str, bm: str, actyear: str, workbook=None):
        from enviroment import project_dir
        import os
        fullfilename = project_dir + os.sep + "template" + os.sep + "exportscore_template.xlsx"
        if not os.path.exists(fullfilename):
            raise Exception("模板文件不存在")
        # print(fullfilename)
        wb = xlrd.open_workbook(fullfilename)
        sh = wb.sheet_by_index(0)
        columns = sh.row_values(0)
        from logic.course_evaluate.CourseEvaluate import CourseEvaluateLogic
        cel = CourseEvaluateLogic()
        result, num, msg = cel.get_ce_fis_sis(schemeid=schemeid)
        scheme = result
        if scheme is None:
            raise Exception("评价指标id错误")
        # print(class2json(result))
        # print(num)
        from logic.score.Score import ScoreLogic
        sl = ScoreLogic()
        query = {"schemeid": schemeid.strip()}
        bm = str(bm).strip()
        if len(bm) > 0:
            query["kkxy"] = str(bm).strip()
        if len(actyear) > 0:
            query["actyear"] = str(actyear).strip()
        result, num, msg = sl.search_no_page(query=query)
        # print(class2json(result))
        # print(len(result))
        scores = result
        # 创建一个workbook 设置编码
        if workbook is None:
            workbook = xlwt.Workbook(encoding='utf-8')
        # 创建一个worksheet
        worksheet = workbook.add_sheet(scheme["name"])
        # 写入excel
        # 参数对应 行, 列, 值
        if "name" in scheme:
            # worksheet.write(0, 0, label=scheme["name"])
            pass
        for index, column in enumerate(columns):
            worksheet.write(0, index, label=str(column).strip())
        columnnum = len(columns)
        if "first_index" in scheme:
            fis: list = scheme["first_index"]
            for index, fi in enumerate(fis):
                worksheet.write(0, columnnum + index * 4, label=str(fi["name"]).strip())
                worksheet.write(0, columnnum + index * 4 + 1, label=str(fi["name"]).strip() + "所占比例")
                worksheet.write(0, columnnum + index * 4 + 2, label=str(fi["name"]).strip() + "等价分数")
                worksheet.write(0, columnnum + index * 4 + 3, label=str(fi["name"]).strip() + "得分")
        if len(scores) > 0:
            tags = sh.row_values(1)
            for score_num, score in enumerate(scores):
                # score: dict = scores[0]
                # print(score)
                for index, tag in enumerate(tags):
                    replace_tag = str(tag).strip().replace("'", "").replace('<$', "").replace('>', '')
                    if replace_tag.lower() == "score_user_info.name":
                        worksheet.write(score_num + 1, index, label=str(score["score_user_info"]["name"]).strip())
                    elif replace_tag.lower() == "scheme_name":
                        worksheet.write(score_num + 1, index, label=str(scheme["name"]).strip())
                    else:
                        if replace_tag in score:
                            # print(replace_tag, ":", score[replace_tag])
                            worksheet.write(score_num + 1, index, label=str(score[replace_tag]).strip())
                        else:
                            worksheet.write(score_num + 1, index, label=str(tag).strip())
                # print("result" in score) and (len(score["result"]) > 0)
                if ("result" in score) and (len(score["result"]) > 0):
                    for index2, fi in enumerate(fis):
                        for r in score["result"]:
                            # print("fi" in r and "_id" in fi)
                            if "fi" in r and "_id" in fi:
                                result_fi_id = r["fi"]["id"]
                                # print(str(result_fi_id).strip() == str(fi["_id"]).strip())
                                if str(result_fi_id).strip() == str(fi["_id"]).strip():
                                    if "name" in r["si"]:
                                        worksheet.write(score_num + 1, columnnum + index2 * 4,
                                                        label=str(r["si"]["name"]).strip())
                                    elif len(r["si"]) > 0 and "name" in r["si"][0]:
                                        worksheet.write(score_num + 1, columnnum + index2 * 4,
                                                        label=str(r["si"][0]["name"]).strip())
                                    if "proportion" in r["fi"]:
                                        worksheet.write(score_num + 1, columnnum + index2 * 4 + 1,
                                                        label=str(r["fi"]["proportion"]).strip() + "%")
                                    if "value" in r["si"]:
                                        worksheet.write(score_num + 1, columnnum + index2 * 4 + 2,
                                                        label=str(r["si"]["value"]))
                                    elif len(r["si"]) > 0 and "value" in r["si"][0]:
                                        worksheet.write(score_num + 1, columnnum + index2 * 4 + 2,
                                                        label=str(r["si"][0]["value"]))
                                    if "value" in r["si"] and "proportion" in r["fi"]:
                                        worksheet.write(score_num + 1, columnnum + index2 * 4 + 3,
                                                        label=int(str(r["fi"]["proportion"])) * int(
                                                            str(r["si"]["value"])) / 100)
                                    elif len(r["si"]) > 0 and "value" in r["si"][0] and "proportion" in r["fi"]:
                                        worksheet.write(score_num + 1, columnnum + index2 * 4 + 3,
                                                        label=int(str(r["fi"]["proportion"])) * int(str(
                                                            r["si"][0]["value"])) / 100)

        return workbook
