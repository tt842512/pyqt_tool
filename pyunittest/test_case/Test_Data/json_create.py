
import json



json_all  =[]


def process_to_json(json_list):
    list_json = json_list
    release_dirt = {'发布原因':'test','发布人':'test','发布工程名称':'test','发布版本':'test','发布类型':'test'}
    release_dirt['发布原因'] = list_json[0]
    release_dirt['发布人'] = list_json[1]
    release_dirt['发布工程名称'] = list_json[2]
    release_dirt['发布版本'] = list_json[3]
    release_dirt['发布类型'] = list_json[4]
    print(release_dirt)
    json_all.append(release_dirt)



def process_json():
    json_dirt = {"发布列表": json_all}
    json_str = json.dumps(json_dirt)
    f = open('release_note.json', 'w')
    f.write(json_str)
    f.close()

testlist = []
process_to_json(testlist)
process_json()