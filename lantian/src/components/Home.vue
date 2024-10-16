<template>
  <el-text>测试页面</el-text>
  <br /><br /><br />

  <el-button @click="open">{{ word }}</el-button>
  <el-text class="mx-1" v-if="seem"
    >预计行程：2024-10-26：<el-link
      href="https://map.baidu.com/poi/%E5%B9%BF%E5%B7%9E%E5%B8%82%C2%B7%E4%BF%A1%E4%B9%89%E4%BC%9A%E9%A6%8621%E6%A0%8B/@12607046.631183783,2629521.9826490926,13z?uid=2d9e6512c948998e4354d7b7&ugc_type=3&ugc_ver=1&device_ratio=2&compat=1&pcevaname=pc4.1&querytype=detailConInfo&da_src=shareurl"
      target="_black"
      >广州tho</el-link
    >
  </el-text>

  <el-form :inline="true" :model="formInline">
    <el-alert title="答对了" type="success" v-if="alertTrue" />
    <el-alert title="请再次尝试" type="error" v-if="alertFalse" />
    <el-form-item label="输入谜底">
      <el-input v-model="formInline.puzzle" />
      <el-button type="primary" @click="submit">提交</el-button>
      <el-button :disabled="button" @click="closeButton">{{ buttonWord }}</el-button>
      <el-button @click="deleteButton">清除数据</el-button>
      <el-text v-if="answer">答对了：是 铃仙</el-text>
    </el-form-item>
  </el-form>

  <el-drawer v-model="drawer" title="谜题一" :with-header="false">
    <span>答对了</span>
  </el-drawer>
</template>

<script lang="ts" setup name="Home">
import { ref } from 'vue'

//行程
const seem = ref(true)
const word = ref('关闭')
const open = () => {
  if (seem.value) {
    seem.value = false
    word.value = '开启'
  } else {
    seem.value = true
    word.value = '关闭'
  }
}

const formInline = ref({
  //谜题答案储存
  puzzle: ''
})
const drawer = ref(false) //橱窗开关
const answer = ref(false) //答案开关
const button = ref(true) //答案按钮
const buttonWord = ref('请努力尝试') //答案按钮字
const buttonData = ref() //历史解答
const alertTrue = ref(false) //回答成功提示
const alertFalse = ref(false)
const submit = () => {
  if (formInline.value.puzzle === '铃仙') {
    drawer.value = true //橱窗打开
    answer.value = true //答案打开
    button.value = false //答案按钮打开
    buttonWord.value = '关闭'
    localStorage.setItem(buttonData.value, '1') //历史记录
    alertTrue.value = true
    setTimeout(() => {
      alertTrue.value = false
    }, 1500)
  } else {
    alertFalse.value = true
    setTimeout(() => {
      alertFalse.value = false
    }, 1500)
  }
}
const closeButton = () => {
  if (answer.value) {
    answer.value = false
    buttonWord.value = '开启'
  } else {
    answer.value = true
    buttonWord.value = '关闭'
  }
}
window.onload = () => {
  if (localStorage.getItem(buttonData.value) == '1') {
    button.value = false
    answer.value = true
    buttonWord.value = '关闭'
  }
}
const deleteButton = () => {
  localStorage.removeItem(buttonData.value)
}
</script>
<style scoped></style>
