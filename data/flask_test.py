from flask import Flask, request
from flask_cors import CORS, cross_origin
import pandas as pd
import networkx as nx
import json
from networkx.readwrite import json_graph
import random



app = Flask(__name__)
cors = CORS(app, resources={r"/foo": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

df_complete = pd.read_csv('01_Processed Data/Complete-Data.csv')
with open('02_Graph/MasterConceptNetwork_Baseline-Test.json') as f:
    js_graph = json.load(f)
    G_MasterConceptNetwork = json_graph.node_link_graph(js_graph)

# @app.route("/<concept>",methods=['GET','POST'])
# def List_Semantic_Feature(concept):
#     feature_list = list(df_complete[df_complete['Concept']==str(concept)].sort_values(by=['cue_validity'],ascending=False)['Feature'])
#     if request.method == 'GET':
#         return feature_list[0]
#     else:
#         return 'POST'

@app.route("/experimentProgress",methods=['GET','POST'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def Experiment_Progress():
    experiment_progress = {
        "current":0,
        "PN_ImageAmount":120,
        "SFAData":[
            {
                "date": "2022-02-18",
                "dose": 18.9,
            },
            {
                "date": "2022-02-19",
                "dose": 28.8,
            },
            {
                "date": "2022-02-20",
                "dose": 39.3,
            },
            {
                "date": "2022-02-22",
                "dose": 81.4,
            },
            {
                "date": "2022-02-23",
                "dose": 47,
            },
            {
                "date": "2022-02-24",
                "dose": 20.3,
            },
            {
                "date": "2022-02-25",
                "dose": 24,
            },
            {
                "date": "2022-02-28",
                "dose": 35.6,
            },
        ],
    }
    return experiment_progress



@app.route("/therapyRecord",methods=['GET','POST'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def Therapy_Record():
    therapy_record = {
        "TherapyRecord":[
            {
            "id":"拖鞋",
            "PictureNaming":[{
                "result":"false",
                "time":20.0,
                "date":"2022-02-28"
            },{
                "result":"true",
                "time":3.2,
                "date":"2022-03-12"
            },],
            "SFA":[{
                "reaction":[{
                    "relationship":"属于",
                    "feature":"交通工具",
                },{
                    "relationship":"能够",
                    "feature":"驾驶",
                },],
                "date":"2022-02-28"
            },{
                "reaction":[{
                    "relationship":"属于",
                    "feature":"交通工具",
                },{
                    "relationship":"能够",
                    "feature":"驾驶",
                },],
                "date":"2022-02-28"
            },],
            "SFAPlan":"true",
            },{
            "id":"鞋垫",
            "PictureNaming":[{
                "result":"false",
                "time":20.0,
                "date":"2022-02-28"
            },{
                "result":"true",
                "time":3.2,
                "date":"2022-03-12"
            },],
            "SFA":[{
                "reaction":[{
                    "relationship":"属于",
                    "feature":"交通工具",
                },{
                    "relationship":"能够",
                    "feature":"驾驶",
                },],
                "date":"2022-02-28"
            },{
                "reaction":[{
                    "relationship":"属于",
                    "feature":"交通工具",
                },{
                    "relationship":"能够",
                    "feature":"驾驶",
                },],
                "date":"2022-02-28"
            },],
            "SFAPlan":"false",
            }
        ]
    }
    return therapy_record



@app.route("/therapyPlan/<para>",methods=['GET','POST'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def Therapy_Plan(para):
    plan_a = {"plans": [
        {
            "type":"subgraph",
            "title": "训练路径 1",
            "checked": "false",
            "nodes": [{
                "id": "钢笔"
            }, {
                "id": "画笔"
            }, {
                "id": "画纸"
            }, {
                "id": "记号笔"
            }, {
                "id": "蜡笔"
            }, {
                "id": "手"
            }, {
                "id": "手臂"
            }, {
                "id": "手掌"
            }, {
                "id": "手指"
            }, {
                "id": "臀部"
            }],
            "edges": [{
                "source": "钢笔",
                "target": "画笔"
            }, {
                "source": "钢笔",
                "target": "画纸"
            }, {
                "source": "钢笔",
                "target": "记号笔"
            }, {
                "source": "钢笔",
                "target": "蜡笔"
            }, {
                "source": "钢笔",
                "target": "手"
            }, {
                "source": "钢笔",
                "target": "手臂"
            }, {
                "source": "钢笔",
                "target": "手掌"
            }, {
                "source": "钢笔",
                "target": "手指"
            }, {
                "source": "画笔",
                "target": "画纸"
            }, {
                "source": "画笔",
                "target": "记号笔"
            }, {
                "source": "画笔",
                "target": "蜡笔"
            }, {
                "source": "画笔",
                "target": "手"
            }, {
                "source": "画笔",
                "target": "手臂"
            }, {
                "source": "画笔",
                "target": "手掌"
            }, {
                "source": "画笔",
                "target": "手指"
            }, {
                "source": "画纸",
                "target": "记号笔"
            }, {
                "source": "画纸",
                "target": "蜡笔"
            }, {
                "source": "画纸",
                "target": "手"
            }, {
                "source": "画纸",
                "target": "手臂"
            }, {
                "source": "画纸",
                "target": "手掌"
            }, {
                "source": "画纸",
                "target": "手指"
            }, {
                "source": "记号笔",
                "target": "蜡笔"
            }, {
                "source": "记号笔",
                "target": "手"
            }, {
                "source": "记号笔",
                "target": "手臂"
            }, {
                "source": "记号笔",
                "target": "手掌"
            }, {
                "source": "记号笔",
                "target": "手指"
            }, {
                "source": "蜡笔",
                "target": "手"
            }, {
                "source": "蜡笔",
                "target": "手臂"
            }, {
                "source": "蜡笔",
                "target": "手掌"
            }, {
                "source": "蜡笔",
                "target": "手指"
            }, {
                "source": "手",
                "target": "手臂"
            }, {
                "source": "手",
                "target": "手掌"
            }, {
                "source": "手",
                "target": "手指"
            }, {
                "source": "手",
                "target": "臀部"
            }, {
                "source": "手臂",
                "target": "手掌"
            }, {
                "source": "手臂",
                "target": "手指"
            }, {
                "source": "手臂",
                "target": "臀部"
            }, {
                "source": "手掌",
                "target": "手指"
            }, {
                "source": "手掌",
                "target": "臀部"
            }, {
                "source": "手指",
                "target": "臀部"
            }]
        },{
            "type":"subgraph",
            "title": "训练路径 2",
            "checked": "false",
            "nodes": [{
                "id": "钢笔"
            }, {
                "id": "画笔"
            }, {
                "id": "画纸"
            }, {
                "id": "记号笔"
            }, {
                "id": "蜡笔"
            }, {
                "id": "手"
            }, {
                "id": "手臂"
            }, {
                "id": "手掌"
            }, {
                "id": "手指"
            }, {
                "id": "臀部"
            }],
            "edges": [{
                "source": "钢笔",
                "target": "画笔"
            }, {
                "source": "钢笔",
                "target": "画纸"
            }, {
                "source": "钢笔",
                "target": "记号笔"
            }, {
                "source": "钢笔",
                "target": "蜡笔"
            }, {
                "source": "钢笔",
                "target": "手"
            }, {
                "source": "钢笔",
                "target": "手臂"
            }, {
                "source": "钢笔",
                "target": "手掌"
            }, {
                "source": "钢笔",
                "target": "手指"
            }, {
                "source": "画笔",
                "target": "画纸"
            }, {
                "source": "画笔",
                "target": "记号笔"
            }, {
                "source": "画笔",
                "target": "蜡笔"
            }, {
                "source": "画笔",
                "target": "手"
            }, {
                "source": "画笔",
                "target": "手臂"
            }, {
                "source": "画笔",
                "target": "手掌"
            }, {
                "source": "画笔",
                "target": "手指"
            }, {
                "source": "画纸",
                "target": "记号笔"
            }, {
                "source": "画纸",
                "target": "蜡笔"
            }, {
                "source": "画纸",
                "target": "手"
            }, {
                "source": "画纸",
                "target": "手臂"
            }, {
                "source": "画纸",
                "target": "手掌"
            }, {
                "source": "画纸",
                "target": "手指"
            }, {
                "source": "记号笔",
                "target": "蜡笔"
            }, {
                "source": "记号笔",
                "target": "手"
            }, {
                "source": "记号笔",
                "target": "手臂"
            }, {
                "source": "记号笔",
                "target": "手掌"
            }, {
                "source": "记号笔",
                "target": "手指"
            }, {
                "source": "蜡笔",
                "target": "手"
            }, {
                "source": "蜡笔",
                "target": "手臂"
            }, {
                "source": "蜡笔",
                "target": "手掌"
            }, {
                "source": "蜡笔",
                "target": "手指"
            }, {
                "source": "手",
                "target": "手臂"
            }, {
                "source": "手",
                "target": "手掌"
            }, {
                "source": "手",
                "target": "手指"
            }, {
                "source": "手",
                "target": "臀部"
            }, {
                "source": "手臂",
                "target": "手掌"
            }, {
                "source": "手臂",
                "target": "手指"
            }, {
                "source": "手臂",
                "target": "臀部"
            }, {
                "source": "手掌",
                "target": "手指"
            }, {
                "source": "手掌",
                "target": "臀部"
            }, {
                "source": "手指",
                "target": "臀部"
            }]
        },{
            "type":"subgraph",
            "title": "训练路径 3",
            "checked": "false",
            "nodes": [{
                "id": "钢笔"
            }, {
                "id": "画笔"
            }, {
                "id": "画纸"
            }, {
                "id": "记号笔"
            }, {
                "id": "蜡笔"
            }, {
                "id": "手"
            }, {
                "id": "手臂"
            }, {
                "id": "手掌"
            }, {
                "id": "手指"
            }, {
                "id": "臀部"
            }],
            "edges": [{
                "source": "钢笔",
                "target": "画笔"
            }, {
                "source": "钢笔",
                "target": "画纸"
            }, {
                "source": "钢笔",
                "target": "记号笔"
            }, {
                "source": "钢笔",
                "target": "蜡笔"
            }, {
                "source": "钢笔",
                "target": "手"
            }, {
                "source": "钢笔",
                "target": "手臂"
            }, {
                "source": "钢笔",
                "target": "手掌"
            }, {
                "source": "钢笔",
                "target": "手指"
            }, {
                "source": "画笔",
                "target": "画纸"
            }, {
                "source": "画笔",
                "target": "记号笔"
            }, {
                "source": "画笔",
                "target": "蜡笔"
            }, {
                "source": "画笔",
                "target": "手"
            }, {
                "source": "画笔",
                "target": "手臂"
            }, {
                "source": "画笔",
                "target": "手掌"
            }, {
                "source": "画笔",
                "target": "手指"
            }, {
                "source": "画纸",
                "target": "记号笔"
            }, {
                "source": "画纸",
                "target": "蜡笔"
            }, {
                "source": "画纸",
                "target": "手"
            }, {
                "source": "画纸",
                "target": "手臂"
            }, {
                "source": "画纸",
                "target": "手掌"
            }, {
                "source": "画纸",
                "target": "手指"
            }, {
                "source": "记号笔",
                "target": "蜡笔"
            }, {
                "source": "记号笔",
                "target": "手"
            }, {
                "source": "记号笔",
                "target": "手臂"
            }, {
                "source": "记号笔",
                "target": "手掌"
            }, {
                "source": "记号笔",
                "target": "手指"
            }, {
                "source": "蜡笔",
                "target": "手"
            }, {
                "source": "蜡笔",
                "target": "手臂"
            }, {
                "source": "蜡笔",
                "target": "手掌"
            }, {
                "source": "蜡笔",
                "target": "手指"
            }, {
                "source": "手",
                "target": "手臂"
            }, {
                "source": "手",
                "target": "手掌"
            }, {
                "source": "手",
                "target": "手指"
            }, {
                "source": "手",
                "target": "臀部"
            }, {
                "source": "手臂",
                "target": "手掌"
            }, {
                "source": "手臂",
                "target": "手指"
            }, {
                "source": "手臂",
                "target": "臀部"
            }, {
                "source": "手掌",
                "target": "手指"
            }, {
                "source": "手掌",
                "target": "臀部"
            }, {
                "source": "手指",
                "target": "臀部"
            }]
        }
    ]}

    plan_b = {"plans": [
       {
            "type":"subgraph",
            "title": "训练路径 1",
            "checked": "false",
            "nodes": [{
                "id": "钢笔"
            }, {
                "id": "画笔"
            }, {
                "id": "画纸"
            }, {
                "id": "记号笔"
            }, {
                "id": "蜡笔"
            }, {
                "id": "手"
            }, {
                "id": "手臂"
            }, {
                "id": "手掌"
            }, {
                "id": "手指"
            }, {
                "id": "臀部"
            }],
            "edges": [{
                "source": "钢笔",
                "target": "画笔"
            }, {
                "source": "钢笔",
                "target": "画纸"
            }, {
                "source": "钢笔",
                "target": "记号笔"
            }, {
                "source": "钢笔",
                "target": "蜡笔"
            }, {
                "source": "钢笔",
                "target": "手"
            }, {
                "source": "钢笔",
                "target": "手臂"
            }, {
                "source": "钢笔",
                "target": "手掌"
            }, {
                "source": "钢笔",
                "target": "手指"
            }, {
                "source": "画笔",
                "target": "画纸"
            }, {
                "source": "画笔",
                "target": "记号笔"
            }, {
                "source": "画笔",
                "target": "蜡笔"
            }, {
                "source": "画笔",
                "target": "手"
            }, {
                "source": "画笔",
                "target": "手臂"
            }, {
                "source": "画笔",
                "target": "手掌"
            }, {
                "source": "画笔",
                "target": "手指"
            }, {
                "source": "画纸",
                "target": "记号笔"
            }, {
                "source": "画纸",
                "target": "蜡笔"
            }, {
                "source": "画纸",
                "target": "手"
            }, {
                "source": "画纸",
                "target": "手臂"
            }, {
                "source": "画纸",
                "target": "手掌"
            }, {
                "source": "画纸",
                "target": "手指"
            }, {
                "source": "记号笔",
                "target": "蜡笔"
            }, {
                "source": "记号笔",
                "target": "手"
            }, {
                "source": "记号笔",
                "target": "手臂"
            }, {
                "source": "记号笔",
                "target": "手掌"
            }, {
                "source": "记号笔",
                "target": "手指"
            }, {
                "source": "蜡笔",
                "target": "手"
            }, {
                "source": "蜡笔",
                "target": "手臂"
            }, {
                "source": "蜡笔",
                "target": "手掌"
            }, {
                "source": "蜡笔",
                "target": "手指"
            }, {
                "source": "手",
                "target": "手臂"
            }, {
                "source": "手",
                "target": "手掌"
            }, {
                "source": "手",
                "target": "手指"
            }, {
                "source": "手",
                "target": "臀部"
            }, {
                "source": "手臂",
                "target": "手掌"
            }, {
                "source": "手臂",
                "target": "手指"
            }, {
                "source": "手臂",
                "target": "臀部"
            }, {
                "source": "手掌",
                "target": "手指"
            }, {
                "source": "手掌",
                "target": "臀部"
            }, {
                "source": "手指",
                "target": "臀部"
            }]
        },{
            "type":"subgraph",
            "title": "训练路径 2",
            "checked": "false",
            "nodes": [{
                "id": "钢笔"
            }, {
                "id": "画笔"
            }, {
                "id": "画纸"
            }, {
                "id": "记号笔"
            }, {
                "id": "蜡笔"
            }, {
                "id": "手"
            }, {
                "id": "手臂"
            }, {
                "id": "手掌"
            }, {
                "id": "手指"
            }, {
                "id": "臀部"
            }],
            "edges": [{
                "source": "钢笔",
                "target": "画笔"
            }, {
                "source": "钢笔",
                "target": "画纸"
            }, {
                "source": "钢笔",
                "target": "记号笔"
            }, {
                "source": "钢笔",
                "target": "蜡笔"
            }, {
                "source": "钢笔",
                "target": "手"
            }, {
                "source": "钢笔",
                "target": "手臂"
            }, {
                "source": "钢笔",
                "target": "手掌"
            }, {
                "source": "钢笔",
                "target": "手指"
            }, {
                "source": "画笔",
                "target": "画纸"
            }, {
                "source": "画笔",
                "target": "记号笔"
            }, {
                "source": "画笔",
                "target": "蜡笔"
            }, {
                "source": "画笔",
                "target": "手"
            }, {
                "source": "画笔",
                "target": "手臂"
            }, {
                "source": "画笔",
                "target": "手掌"
            }, {
                "source": "画笔",
                "target": "手指"
            }, {
                "source": "画纸",
                "target": "记号笔"
            }, {
                "source": "画纸",
                "target": "蜡笔"
            }, {
                "source": "画纸",
                "target": "手"
            }, {
                "source": "画纸",
                "target": "手臂"
            }, {
                "source": "画纸",
                "target": "手掌"
            }, {
                "source": "画纸",
                "target": "手指"
            }, {
                "source": "记号笔",
                "target": "蜡笔"
            }, {
                "source": "记号笔",
                "target": "手"
            }, {
                "source": "记号笔",
                "target": "手臂"
            }, {
                "source": "记号笔",
                "target": "手掌"
            }, {
                "source": "记号笔",
                "target": "手指"
            }, {
                "source": "蜡笔",
                "target": "手"
            }, {
                "source": "蜡笔",
                "target": "手臂"
            }, {
                "source": "蜡笔",
                "target": "手掌"
            }, {
                "source": "蜡笔",
                "target": "手指"
            }, {
                "source": "手",
                "target": "手臂"
            }, {
                "source": "手",
                "target": "手掌"
            }, {
                "source": "手",
                "target": "手指"
            }, {
                "source": "手",
                "target": "臀部"
            }, {
                "source": "手臂",
                "target": "手掌"
            }, {
                "source": "手臂",
                "target": "手指"
            }, {
                "source": "手臂",
                "target": "臀部"
            }, {
                "source": "手掌",
                "target": "手指"
            }, {
                "source": "手掌",
                "target": "臀部"
            }, {
                "source": "手指",
                "target": "臀部"
            }]
        }
    ]}

    if random.random()>0.5:
        return plan_a
    else:
        return plan_b


@app.route("/shortestPath/<concept>",methods=['GET','POST'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def Shortest_Path(concept):
    target_maincategory = df_complete[df_complete['Concept']==concept]['上级类别'].unique()[0]

    nodes = []
    for n in G_MasterConceptNetwork.nodes:
        if 'picture_naming_result' in G_MasterConceptNetwork.nodes[n]:
            if (G_MasterConceptNetwork.nodes[n]['maincategory']==target_maincategory) & (G_MasterConceptNetwork.nodes[n]['picture_naming_result']==True):
                nodes.append(n)

    shortest_length = 1000
    shortest_path = []

    for node in nodes:
        path = nx.dijkstra_path(G_MasterConceptNetwork, node, concept)
        if(len(path)<shortest_length):
            shortest_length = len(path)
            shortest_path = path
        subgraph = G_MasterConceptNetwork.subgraph(shortest_path)


    return json.dumps(json_graph.node_link_data(subgraph),ensure_ascii=False).replace('links','edges')


@app.route("/nodeRecord/<concept>",methods=['GET','POST'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def Node_Record(concept):
    node_record = {
        "id":concept,
        "PictureNaming":[{
            "result":"false",
            "time":20.0,
            "date":"2022-02-28"
        },{
            "result":"true",
            "time":3.2,
            "date":"2022-03-12"
        },],
        "SFA":[{
            "reaction":[{
                "relationship":"属于",
                "feature":"交通工具",
            },{
                "relationship":"能够",
                "feature":"驾驶",
            },],
            "date":"2022-02-28"
        },{
            "reaction":[{
                "relationship":"属于",
                "feature":"交通工具",
            },{
                "relationship":"能够",
                "feature":"驾驶",
            },],
            "date":"2022-02-28"
        }
        ]
    }
    return node_record



@app.route("/planGraph",methods=['GET','POST'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def Plan_Graph():
    plan_graph = {
        "nodes": [{
            "subcategory": "工具",
            "maincategory": "人造物",
            "id": "钢笔"
        }, {
            "subcategory": "工具",
            "maincategory": "人造物",
            "id": "画笔"
        }, {
            "subcategory": "工具",
            "maincategory": "人造物",
            "id": "画纸"
        }, {
            "subcategory": "工具",
            "maincategory": "人造物",
            "id": "记号笔"
        }, {
            "subcategory": "工具",
            "maincategory": "人造物",
            "id": "蜡笔"
        }, {
            "subcategory": "身体部位",
            "maincategory": "身体部位",
            "id": "手"
        }, {
            "subcategory": "身体部位",
            "maincategory": "身体部位",
            "id": "手臂"
        }, {
            "subcategory": "身体部位",
            "maincategory": "身体部位",
            "id": "手掌"
        }, {
            "subcategory": "身体部位",
            "maincategory": "身体部位",
            "id": "手指"
        }, {
            "subcategory": "身体部位",
            "maincategory": "身体部位",
            "id": "臀部"
        }],
        "edges": [{
            "weight": 1.0,
            "source": "钢笔",
            "target": "钢笔"
        }, {
            "weight": 0.833563665,
            "source": "钢笔",
            "target": "画笔"
        }, {
            "weight": 0.729334454,
            "source": "钢笔",
            "target": "画纸"
        }, {
            "weight": 0.806783151,
            "source": "钢笔",
            "target": "记号笔"
        }, {
            "weight": 0.789160661,
            "source": "钢笔",
            "target": "蜡笔"
        }, {
            "weight": 0.461681547,
            "source": "钢笔",
            "target": "手"
        }, {
            "weight": 0.522326804,
            "source": "钢笔",
            "target": "手臂"
        }, {
            "weight": 0.452785838,
            "source": "钢笔",
            "target": "手掌"
        }, {
            "weight": 0.503370717,
            "source": "钢笔",
            "target": "手指"
        }, {
            "weight": 1.0,
            "source": "画笔",
            "target": "画笔"
        }, {
            "weight": 0.824119591,
            "source": "画笔",
            "target": "画纸"
        }, {
            "weight": 0.904647908,
            "source": "画笔",
            "target": "记号笔"
        }, {
            "weight": 0.868122534,
            "source": "画笔",
            "target": "蜡笔"
        }, {
            "weight": 0.524525185,
            "source": "画笔",
            "target": "手"
        }, {
            "weight": 0.594872923,
            "source": "画笔",
            "target": "手臂"
        }, {
            "weight": 0.513030702,
            "source": "画笔",
            "target": "手掌"
        }, {
            "weight": 0.577260057,
            "source": "画笔",
            "target": "手指"
        }, {
            "weight": 1.0,
            "source": "画纸",
            "target": "画纸"
        }, {
            "weight": 0.740142568,
            "source": "画纸",
            "target": "记号笔"
        }, {
            "weight": 0.913701008,
            "source": "画纸",
            "target": "蜡笔"
        }, {
            "weight": 0.540371419,
            "source": "画纸",
            "target": "手"
        }, {
            "weight": 0.577401642,
            "source": "画纸",
            "target": "手臂"
        }, {
            "weight": 0.532365153,
            "source": "画纸",
            "target": "手掌"
        }, {
            "weight": 0.571582634,
            "source": "画纸",
            "target": "手指"
        }, {
            "weight": 1.0,
            "source": "记号笔",
            "target": "记号笔"
        }, {
            "weight": 0.806684534,
            "source": "记号笔",
            "target": "蜡笔"
        }, {
            "weight": 0.460387208,
            "source": "记号笔",
            "target": "手"
        }, {
            "weight": 0.499090958,
            "source": "记号笔",
            "target": "手臂"
        }, {
            "weight": 0.453705377,
            "source": "记号笔",
            "target": "手掌"
        }, {
            "weight": 0.500626342,
            "source": "记号笔",
            "target": "手指"
        }, {
            "weight": 1.0,
            "source": "蜡笔",
            "target": "蜡笔"
        }, {
            "weight": 0.563729515,
            "source": "蜡笔",
            "target": "手"
        }, {
            "weight": 0.605572089,
            "source": "蜡笔",
            "target": "手臂"
        }, {
            "weight": 0.555566419,
            "source": "蜡笔",
            "target": "手掌"
        }, {
            "weight": 0.600878023,
            "source": "蜡笔",
            "target": "手指"
        }, {
            "weight": 1.0,
            "source": "手",
            "target": "手"
        }, {
            "weight": 0.852983229,
            "source": "手",
            "target": "手臂"
        }, {
            "weight": 0.864065397,
            "source": "手",
            "target": "手掌"
        }, {
            "weight": 0.887756355,
            "source": "手",
            "target": "手指"
        }, {
            "weight": 0.585001422,
            "source": "手",
            "target": "臀部"
        }, {
            "weight": 1.0,
            "source": "手臂",
            "target": "手臂"
        }, {
            "weight": 0.883878504,
            "source": "手臂",
            "target": "手掌"
        }, {
            "weight": 0.916958628,
            "source": "手臂",
            "target": "手指"
        }, {
            "weight": 0.684903322,
            "source": "手臂",
            "target": "臀部"
        }, {
            "weight": 1.0,
            "source": "手掌",
            "target": "手掌"
        }, {
            "weight": 0.804232548,
            "source": "手掌",
            "target": "手指"
        }, {
            "weight": 0.625284889,
            "source": "手掌",
            "target": "臀部"
        }, {
            "weight": 1.0,
            "source": "手指",
            "target": "手指"
        }, {
            "weight": 0.625265234,
            "source": "手指",
            "target": "臀部"
        }, {
            "weight": 1.0,
            "source": "臀部",
            "target": "臀部"
        }]
    }

    return plan_graph


@app.route("/nodeInfo/<concept>",methods=['GET','POST'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def Node_Info(concept):
    node_info={
        "id":"摩托车",
        "maincategory":"交通工具",
        "subcategory":"车辆",
        "features": {
            "范畴": ["车", "船", "飞机"],
            "用途": ["行驶", "乘坐", "开", "骑"],
            "动作": ["司机", "维护", "修理", "加油"],
            "属性": ["方向盘", "车身", "车厢", "仪表盘"],
            "场所": [],
            "联想": ["房屋", "货车", "轿车", "电动车"]
        }
    }
    return node_info

@app.route("/edgeInfo/<parameters>",methods=['GET','POST'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def Edge_Info(parameters):
    edge_info={
        "source":"画笔",
        "target":"手臂",
        "shared_features": {
            "范畴": ["车", "船", "飞机"],
            "用途": ["行驶", "乘坐", "开", "骑"],
            "动作": ["司机", "维护", "修理", "加油"],
            "属性": ["方向盘", "车身", "车厢", "仪表盘"],
            "场所": [],
            "联想": ["房屋", "货车", "轿车", "电动车"]
        }
    }
    return edge_info