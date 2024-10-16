<template>
  <el-timeline style="width: 100%">
    <el-timeline-item
      :data="activities"
      v-for="(activity, index) in activities"
      :key="index"
      :timestamp="activity.timestamp"
      placement="top"
    >
      {{ activity.contant }}
    </el-timeline-item>
  </el-timeline>
</template>

<script lang="ts" setup name="Web">
import { ref } from 'vue'

interface Web {
  timestamp: string
  contant: string
}

const drawer = ref(false)

const activities: Web[] = [
  {
    timestamp: '2024-10-10',
    contant: '创建网站\n创建首页、日记按钮\n初步日记按钮--东方记录'
  },
  {
    timestamp: '2024-10-12',
    contant: '完善日记按钮-东方记录'
  }
]
</script>

<style scoped></style>
