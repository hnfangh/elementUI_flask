
<template>
  <div>
    <!-- Head -->
    <el-breadcrumb separator="/">
      <el-breadcrumb-item :to="{ path: '/' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item>用户列表</el-breadcrumb-item>
    </el-breadcrumb>

    <!-- Table -->
    <el-table :data="tableData" height="250" border style="width: 100%">
      <el-table-column prop="id" label="序号" width="50"></el-table-column>
      <el-table-column prop="name" label="姓名" width="100"></el-table-column>
      <el-table-column prop="age" label="年龄" width="100"></el-table-column>
      <el-table-column prop="date" label="生日" width="180"></el-table-column>
      <el-table-column prop="edit" label="操作">
        <template slot-scope="scope">
          <el-button @click="searchuser(scope.row)" type="text" size="small">查看</el-button>
          <el-button @click="edituser(scope.row,scope.$index)" type="text" size="small">编辑</el-button>
          <el-button @click.native.prevent="delereopen(scope.$index, scope.row.id)" type="text" size="small">删除</el-button>
        </template>
      </el-table-column>
    </el-table>

    <!-- Aialog 添加用户-->
    <el-button type="primary" style="float:left" @click="dialogFormVisible = true">添加用户</el-button>
    <el-dialog title="添加用户信息" :visible.sync="dialogFormVisible">
      <el-form :model="form">
        <el-form-item label="输入用户名" label-width="180">
          <el-input v-model="form.name" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="输入年龄" label-width="180">
          <el-input v-model="form.age" type="number" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="选择出生年月" label-width="180">
          <el-date-picker v-model="form.date" type="date" placeholder="选择日期"></el-date-picker>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogFormVisible = false">取 消</el-button>
        <el-button type="primary" @click="adduser">确 定</el-button>
      </div>
    </el-dialog>

    <!-- Aialog 编辑用户-->
    <el-dialog title="编辑用户信息" :visible.sync="editdialogFormVisible">
      <el-form :model="editform">
        <el-form-item label="输入用户名" label-width="180">
          <el-input v-model="editform.name" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="输入年龄" label-width="180">
          <el-input v-model="editform.age" type="number" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="选择出生年月" label-width="180">
          <el-date-picker v-model="editform.date" type="date" placeholder="选择日期"></el-date-picker>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="editdialogFormVisible = false">取 消</el-button>
        <el-button type="primary" @click="updateuser">更 新</el-button>
      </div>
    </el-dialog>

    <!-- Aialog 查看用户-->
    <el-dialog title="查看用户信息" :visible.sync="searchdialogFormVisible">
      <el-form :model="searchform">
        <el-form-item label="输入用户名" label-width="180">
          <el-input v-model="searchform.name" autocomplete="off" :disabled="true"></el-input>
        </el-form-item>
        <el-form-item label="输入年龄" label-width="180">
          <el-input v-model="searchform.age" type="number" autocomplete="off" :disabled="true"></el-input>
        </el-form-item>
        <el-form-item label="选择出生年月" label-width="180">
          <el-date-picker v-model="searchform.date" type="date" placeholder="选择日期" :disabled="true"></el-date-picker>
        </el-form-item>
      </el-form>
    </el-dialog>
  </div>
</template>


<script>
import axios from "axios";
import dateFormat from "./Utils";
export default {
  name: "UserInfo",
  methods: {
    //查看用户
    searchuser(row) {
      this.searchdialogFormVisible = true;
      this.searchform = row;
      console.log(row);
    },
    //编辑用户
    edituser(row, index) {
      this.editIndex = index;
      this.editform = row;
      this.editdialogFormVisible = true;
    },
    //更新用户
    updateuser() {
      let _this = this;
      let { name, age, date } = this.editform;
      let { id } = this.tableData[this.editIndex];
      let d = dateFormat("YYYY-mm-dd", date);
      axios
        .post("http://127.0.0.1:5000/updateuser", {
          id,
          name,
          age,
          date: d
        })
        .then(function(response) {
          _this.$set(_this.tableData, _this.editIndex, {
            id,
            name,
            age,
            date: d
          });
          _this.editdialogFormVisible = false;
        });
    },
    //删除用户
    deleteuser(index, id) {
      let _this = this;
      axios
        .post("http://127.0.0.1:5000/deleteuser", {
          id
        })
        .then(function(response) {
          _this.tableData.splice(index, 1);
        });
    },
    //删除弹窗
    delereopen(index,id) {
        this.$alert('确定删除这条信息？', '删除信息', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          callback: action => {
              console.log(action)
              if(action == "confirm"){
                this.deleteuser(index,id)
              }
          }
        });
    },
    //添加用户
    adduser() {
      let len = this.tableData.length;
      let { name, age, date } = this.form;
      axios
        .post("http://127.0.0.1:5000/adduser", {
          id: len + 1,
          name,
          age,
          date: dateFormat("YYYY-mm-dd", date)
        })
        .then(function(response) {
          console.log(response);
        });
      this.tableData.push({
        id: len + 1,
        name,
        age,
        date: dateFormat("YYYY-mm-dd", date)
      });
      this.form = {
        name: "",
        age: "",
        date: ""
      };
      this.dialogFormVisible = false;
    },

    //查询用户
    searchlist(){
      let _this = this
      axios.post("http://127.0.0.1:5000/userlist",{
      }).then(function(response){
        console.log(response)
        let data  =JSON.parse(response.data)
        console.log(data)
        _this.tableData = [...data]
      })
    }
  },

  // 提前调用
  created(){
    this.searchlist()
  },



  data() {
    return {
      editIndex: 0,
      tableData: [],
      searchdialogFormVisible: false,
      dialogFormVisible: false,
      editdialogFormVisible: false,
      deletevisible: false,
      form: {
        name: "",
        age: "",
        date: ""
      },
      editform: {
        name: "",
        age: "",
        date: ""
      },
      searchform: {
        name: "",
        age: "",
        date: ""
      },
      pickerOptions: {
        disabledDate(time) {
          return time.getTime() > Date.now();
        }
      }
    };
  }
};
</script>


<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1,
h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
