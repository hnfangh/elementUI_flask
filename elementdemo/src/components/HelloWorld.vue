<template>
  <el-row>
    <el-col :span="12">
      <div class="grid-content bg-purple">
        <el-input v-model="input1" placeholder="请输入用户名"></el-input>
        <el-input v-model="input2" placeholder="请输入密码"></el-input>
        <el-input v-model="input3" placeholder="请输入城市名字"></el-input>
        <el-input v-model="input4" placeholder="请输入查询类型(1.当天 2.未来7天 3.未来8-15天)"></el-input>
      </div>
    </el-col>
    <el-col :span="12">
      <div class="grid-content bg-purple-light">
        <el-button v-on:click="login">用户登陆</el-button>
        <el-button v-on:click="search">查询天气</el-button>
      </div>
    </el-col>
  </el-row>
</template>

<script>
import axios from "axios"
export default {
  name: "HelloWorld",
  data() {
    return {
      input1: '',
      input2: '',
      input3: '',
      input4: ''
    };  
  },

  methods:{
    login: function(){
      alert('用户名:'+this.input1+' 密码:'+this.input2)
      axios.post('http://127.0.0.1:5000/test',{
        username: this.input1,
        password: this.input2
      })
      .then(function (response) {
      console.log(response);
      })
      .catch(function (error) {
      console.log(error);
      });

    },
    search: function(){
      alert('城市名'+this.input3+' 查询类型:'+this.input4)
      axios.post('http://127.0.0.1:5000/weather',{
        city: this.input3,
        type: this.input4
    })
    .then(function (response) {
    console.log(response);
    })
    .catch(function (error) {
    console.log(error);
    });

    }


  }

}
  
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
