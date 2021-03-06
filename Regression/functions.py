import csv
from django.http import HttpResponse

import numpy as np
import pandas as pd
import sklearn
import pickle
import os

### Process csv files
def process_files(test_x):
    #データ読み込み
    x_test_df = pd.read_csv(test_x, sep=',')


    #予測
    this_folder = os.path.dirname(os.path.abspath(__file__))
    saved_model = os.path.join(this_folder, 'rfr_model.sav')
    rfr = pickle.load(open(saved_model, 'rb'))
    y_pred_test = rfr.predict(x_test_df[['職場の様子','勤務地固定','休日休暇(月曜日)','大手企業','週1日からOK','交通費別途支給','残業月20時間以上','職種コード','1日7時間以下勤務OK','ミドル（40〜）活躍中','ルーティンワークがメイン','短時間勤務OK(1日4h以内)','駅から徒歩5分以内','対象者設定\u3000年齢下限','学校・公的機関（官公庁）','土日祝のみ勤務','Wordのスキルを活かす','給与/交通費\u3000給与支払区分','CAD関連のスキルを活かす','派遣スタッフ活躍中','固定残業制','大量募集','公開区分','20代活躍中','Accessのスキルを活かす','検索対象エリア','就業形態区分','休日休暇(火曜日)','平日休みあり','30代活躍中','フラグオプション選択','期間・時間\u3000勤務期間','派遣形態','週2・3日OK','勤務先公開','Excelのスキルを活かす','16時前退社OK','正社員登用あり','残業月20時間未満','英語力不要','休日休暇(日曜日)','雇用形態','Dip JobsリスティングS','社員食堂あり','資格取得支援制度あり','対象者設定\u3000年齢上限','10時以降出社OK','社会保険制度あり','英語以外の語学力を活かす','休日休暇(祝日)','外資系企業','服装自由','PowerPointのスキルを活かす','残業月10時間未満','休日休暇(土曜日)','履歴書不要','休日休暇(木曜日)','研修制度あり','英語力を活かす','DTP関連のスキルを活かす','会社概要\u3000業界コード','勤務地\u3000都道府県コード','PCスキル不要','車通勤OK','制服あり','休日休暇(水曜日)','仕事の仕方','紹介予定派遣','シフト勤務','経験者優遇','週4日勤務','未経験OK','土日祝休み','給与/交通費\u3000交通費','新卒・第二新卒歓迎','休日休暇(金曜日)','産休育休取得事例あり','扶養控除内','給与/交通費\u3000給与下限','対象者設定\u3000性別','WEB登録OK','オフィスが禁煙・分煙','勤務地\u3000市区町村コード','残業なし']])

    #結果出力
    ans_df = pd.DataFrame(x_test_df['お仕事No.'])
    ans_df['応募数 合計'] = y_pred_test
    ans_df.to_csv('ans.csv', index=False)
    ans_list = ans_df.values.tolist()

    return ans_list

def csvdownload(ans_list):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="ans.csv"'
    writer = csv.writer(response)

    writer.writerow(['お仕事No.', '応募数 合計'])
    for row in ans_list:
        writer.writerow(row)

    return response
