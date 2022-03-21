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