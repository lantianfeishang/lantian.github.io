<template>
  <el-menu mode="horizontal">
    <el-menu-item index="1">飞上蓝天的博客</el-menu-item>
    <router-link to="/"
      ><el-menu-item index="2"
        ><el-button type="primary">首页</el-button></el-menu-item
      ></router-link
    >
    <el-dropdown>
      <el-menu-item index="3">
        <el-button type="primary">
          日记<el-icon class="el-icon--right"><arrow-down /></el-icon></el-button
      ></el-menu-item>
      <template #dropdown>
        <el-dropdown-menu>
          <router-link to="/DiaryWeb"><el-dropdown-item>网站日志</el-dropdown-item></router-link>
          <router-link to="/DiaryLearn"><el-dropdown-item>学习笔记</el-dropdown-item></router-link>
          <router-link to="/DiaryTouhou"><el-dropdown-item>东方记录</el-dropdown-item></router-link>
        </el-dropdown-menu>
      </template>
    </el-dropdown>
  </el-menu>
  <router-view />
</template>

<script lang="ts" setup name="APP">
import { ArrowDown } from '@element-plus/icons-vue'
</script>

<style scoped></style>
