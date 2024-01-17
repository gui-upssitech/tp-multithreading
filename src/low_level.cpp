#include <cpr/cpr.h>

#include <Eigen/Dense>
#include <iostream>
#include <nlohmann/json.hpp>
using json = nlohmann::json;

std::vector<std::vector<float>> ConvertToVector(Eigen::MatrixXf eMatrix) {
  std::vector<std::vector<float>> data;
  data.resize(eMatrix.rows(), std::vector<float>(eMatrix.cols(), 0));

  for (size_t i = 0; i < data.size(); i++)
    for (size_t j = 0; j < data.front().size(); j++) data[i][j] = eMatrix(i, j);

  return data;
}

Eigen::MatrixXf ConvertToEigenMatrix(std::vector<std::vector<float>> data) {
  Eigen::MatrixXf eMatrix(data.size(), data.front().size());
  for (int i = 0; i < data.size(); ++i)
    eMatrix.row(i) = Eigen::VectorXf::Map(data[i].data(), data.front().size());
  return eMatrix;
}

class Task {
 public:
  std::string id;
  int size;
  float time;
  Eigen::MatrixXf a;
  Eigen::VectorXf b;
  Eigen::VectorXf x;

  Task(json j) {
    this->id = j.at("identifier").get<std::string>();
    this->size = j.at("size").get<int>();
    this->time = j.at("time").get<float>();

    auto aArray = j.at("a").get<std::vector<std::vector<float>>>();
    auto bArray = j.at("b").get<std::vector<float>>();
    auto xArray = j.at("x").get<std::vector<float>>();

    this->a = ConvertToEigenMatrix(aArray);
    this->b = Eigen::VectorXf::Map(bArray.data(), bArray.size());
    this->x = Eigen::VectorXf::Map(xArray.data(), xArray.size());
  }

  void print() {
    // std::cout << "Task" << std::endl;
    std::cout << "- id:" << this->id << std::endl;
    // std::cout << "- size:" << this->size << std::endl;
    // std::cout << "- time:" << this->time << std::endl;
    std::cout << "- a:" << std::endl << this->a << std::endl << std::endl;
    // std::cout << "- b:" << std::endl << this->b << std::endl;
    // std::cout << "- x:" << std::endl << this->x << std::endl;
  }

  void work() {
    // solve Ax = b
    auto start = std::chrono::high_resolution_clock::now();

    // Formule trouvées sur
    // https://eigen.tuxfamily.org/dox/group__LeastSquares.html
    this->x = a.colPivHouseholderQr().solve(b);

    auto end = std::chrono::high_resolution_clock::now();
    this->time =
        std::chrono::duration_cast<std::chrono::nanoseconds>(end - start)
            .count() *
        1e-9;
  }

  json toJson() {
    json j;
    j["identifier"] = id;
    j["size"] = size;
    j["time"] = time;
    j["a"] = ConvertToVector(a);
    j["b"] = std::vector<float>(b.data(), b.data() + b.rows() * b.cols());
    j["x"] = std::vector<float>(x.data(), x.data() + x.rows() * x.cols());
    return j;
  }
};

int main() {
  while (true) {
    auto r = cpr::Get(cpr::Url{"http://localhost:8000"});
    if (r.status_code != 200) continue;

    json j = json::parse(r.text);
    Task task(j);
    std::cout << "Received task #" << task.id << std::endl;

    task.work();

    json response = task.toJson();
    std::cout << "Finished task #" << task.id << " in " << task.time
              << " seconds" << std::endl;

    auto r2 =
        cpr::Post(cpr::Url{"http://localhost:8000"}, cpr::Body{response.dump()},
                  cpr::Header{{"Content-Type", "application/json"}});
  }

  return 0;
}
