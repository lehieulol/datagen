from solver import *
import yaml

class Generator:
    def __init__(self, num_target, q_max=5, r_s=40, r_c=80, r_cl=80, area=1000, rand_q=True, base=[0, 0]):
        np.random.seed(parameter.seed)
        random.seed(parameter.seed)
        parameter.seed += 1
        self.base = Point(base[0], base[1])
        self.num_target = num_target
        self.q_max = q_max
        if rand_q:
            self.q = np.random.randint(1, q_max + 1, num_target).tolist()
        else:
            self.q = [q_max for i in range(num_target)]
        self.targets = []
        self.t_list = np.random.uniform(0, area, (num_target, 2)).tolist()
        for i in range(num_target):
            self.targets.append(Target(self.t_list[i][0], self.t_list[i][1], self.q[i], r_s))
        self.r_s = r_s
        self.r_c = r_c
        self.r_cl = r_cl
        self.area = area
        assert r_cl >= 2 * r_s

    def generate(self, OUTPUT):
        net = Net(self.targets, self.r_s, self.r_c, self.r_cl, self.q, self.base)
        # Phase 1
        net.build_disk_set()
        net.cut_disk_set(k=2)
        net.place_sensor()
        # Phase 2
        net.createCluster()
        net.build_graph()
        net.insert_edge()
        net.place_relay_nodes_in_clusters()
        net.place_relay_nodes_between_centers()

        out_dict = dict()
        out_dict["targets"] = self.t_list
        out_dict["base_station"] = [float(self.base.x), float(self.base.y)]

        out_dict["nodes"] = []
        for sensor in net.sList:
            out_dict["nodes"].append([float(sensor.x), float(sensor.y)])

        for relay in net.relay_nodes:
            out_dict["nodes"].append([float(relay.x), float(relay.y)])

        out_file = open(OUTPUT, "w")
        out_file.write("""# multiple nodes charging model
node_phy_spe:
  "capacity" : 10800
  "threshold" : 540
  "com_range": 80
  "sen_range": 40
  "prob_gp": 1
  # others
  "package_size" : 400.0
  # transmission specifications
  "er" : 0.0001
  "et" : 0.00005
  "efs" : 0.00000001
  "emp" : 0.0000000000013

seed: 0

""")
        yaml.dump(out_dict, out_file)
        out_file.close()
