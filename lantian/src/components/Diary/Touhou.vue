<template>
  <el-table
    :data="tableData"
    :default-sort="{ prop: 'date', order: 'descending' }"
    stripe
    :border="parentBorder"
    height="500"
    style="width: 100%"
  >
    <el-table-column type="index" fixed />
    <el-table-column type="expand">
      <template #default="props">
        <el-table stripe :data="props.row.details" :border="childBorder">
          <el-table-column prop="identity" label="身份" />
          <el-table-column prop="others" label="其他" />
        </el-table>
      </template>
    </el-table-column>
    <el-table-column
      prop="date"
      label="时间"
      sortable
      :filters="[
        { text: '2023', value: '2023' },
        { text: '2024', value: '2024' }
      ]"
      :filter-method="filterHandler"
    >
      <template #default="scope">
        <div style="display: flex; align-items: center">
          <span>{{ scope.row.date }}</span>
        </div>
      </template>
    </el-table-column>
    <el-table-column prop="name" label="名称" />
    <el-table-column prop="place" label="地点">
      <template #default="scope">
        <span style="margin-left: 10px"
          ><el-link :href="scope.row.href" :underline="false" target="_blank">{{
            scope.row.place
          }}</el-link></span
        >
      </template>
    </el-table-column>
  </el-table>
</template>

<script lang="ts" setup name="Touhou">
import type { TableInstance } from 'element-plus'
import { ref } from 'vue'

interface User {
  date: string
  name: string
  place: string
  href: string
  details: [
    {
      identity: string
      others: string
    }
  ]
}

const parentBorder = ref(false)
const childBorder = ref(false)

const tableRef = ref<TableInstance>()
const filterHandler = (value: string, row: User) => {
  return !row.date.indexOf(value)
}

const tableData: User[] = [
  {
    date: '2023/08/10',
    name: '广州tho',
    place: '信义会馆21栋',
    href: 'https://map.baidu.com/poi/%E5%B9%BF%E5%B7%9E%E5%B8%82%C2%B7%E4%BF%A1%E4%B9%89%E4%BC%9A%E9%A6%8621%E6%A0%8B/@12607043.315,2627634.7,19z?uid=2d9e6512c948998e4354d7b7&ugc_type=3&ugc_ver=1&device_ratio=2&compat=1&pcevaname=pc4.1&querytype=detailConInfo&da_src=shareurl',
    details: [
      {
        identity: '游客',
        others: '好评如潮'
      }
    ]
  },
  {
    date: '2023/10/02',
    name: '重庆tho+lp',
    place: '壹街区b区',
    href: 'https://map.baidu.com/search/%E9%A1%BA%E7%A5%A5%C2%B7%E5%A3%B9%E8%A1%97%E5%8C%BA-b%E5%8C%BA/@11854923.116425408,3416778.54535195,19z?querytype=s&da_src=shareurl&wd=%E9%A1%BA%E7%A5%A5%C2%B7%E5%A3%B9%E8%A1%97%E5%8C%BA-B%E5%8C%BA&c=131&src=0&wd2=%E9%87%8D%E5%BA%86%E5%B8%82%E5%A4%A7%E6%B8%A1%E5%8F%A3%E5%8C%BA&pn=0&sug=1&l=13&b=(12274790,2396787;12315558,2415859)&from=webmap&biz_forward=%7B%22scaler%22:2,%22styles%22:%22pl%22%7D&sug_forward=d0959521bc857a63c7f50d95&device_ratio=2',
    details: [
      {
        identity: '游客',
        others: '别了重庆，就像刚来般悸动'
      }
    ]
  },
  {
    date: '2024/02/01',
    name: '金华tho',
    place: '格瑞酒店',
    href: 'https://map.baidu.com/search/%E9%87%91%E5%8D%8E%E6%A0%BC%E7%91%9E%E9%85%92%E5%BA%97/@13318201.966111945,3369262.80951005,19z?querytype=s&da_src=shareurl&wd=%E9%87%91%E5%8D%8E%E6%A0%BC%E7%91%9E%E9%85%92%E5%BA%97&c=132&src=0&pn=0&sug=0&l=19&b=(11854604.616425408,3416629.54535195;11855241.616425408,3416927.54535195)&from=webmap&biz_forward=%7B%22scaler%22:2,%22styles%22:%22pl%22%7D&device_ratio=2',
    details: [
      {
        identity: '摊主static world',
        others: '犹思'
      }
    ]
  },
  {
    date: '2024/02/25',
    name: '大连the+Comic Rise',
    place: '星海国际金融中心',
    href: 'https://map.baidu.com/search/%E6%98%9F%E6%B5%B7%E5%9B%BD%E9%99%85%E9%87%91%E8%9E%8D%E4%B8%AD%E5%BF%83/@13535806.051970912,4679215.93258615,19z?querytype=s&da_src=shareurl&wd=%E6%98%9F%E6%B5%B7%E5%9B%BD%E9%99%85%E9%87%91%E8%9E%8D%E4%B8%AD%E5%BF%83&c=333&src=0&pn=0&sug=0&l=19&b=(13317886.575033674,3369112.255049186;13318523.575033674,3369410.255049186)&from=webmap&biz_forward=%7B%22scaler%22:2,%22styles%22:%22pl%22%7D&device_ratio=2',
    details: [
      {
        identity: '摊主static world',
        others: '逢时逍遥不论时，谈天任君不晓天'
      }
    ]
  },
  {
    date: '2024/05/02',
    name: '深圳tho',
    place: '文博宫',
    href: 'https://map.baidu.com/search/%E6%96%87%E5%8D%9A%E5%AE%AB/@12702630.500642287,2568402.87703925,18.25z?querytype=s&da_src=shareurl&wd=%E6%96%87%E5%8D%9A%E5%AE%AB&c=167&src=0&pn=0&sug=0&l=19&b=(13535487.551970912,4679066.93258615;13536124.551970912,4679364.93258615)&from=webmap&biz_forward=%7B%22scaler%22:2,%22styles%22:%22pl%22%7D&device_ratio=2',
    details: [
      {
        identity: '摊主糕雨铺',
        others: '渐'
      }
    ]
  },
  {
    date: '2024/05/04',
    name: '厦门tho',
    place: '厦门荣誉国际酒店',
    href: 'https://map.baidu.com/search/%E5%8E%A6%E9%97%A8%E8%8D%A3%E8%AA%89%E5%9B%BD%E9%99%85%E9%85%92%E5%BA%97/@13154538.866591297,2790591.0975097,18.79z?querytype=s&da_src=shareurl&wd=%E5%8E%A6%E9%97%A8%E8%8D%A3%E8%AA%89%E5%9B%BD%E9%99%85%E9%85%92%E5%BA%97&c=340&src=0&pn=0&sug=0&l=18&b=(12702093.547253411,2568151.6806344073;12703167.454031162,2568654.0734440926)&from=webmap&biz_forward=%7B%22scaler%22:2,%22styles%22:%22pl%22%7D&device_ratio=2',
    details: [
      {
        identity: '摊主帝组',
        others: '慌慌，逝去，离得匆匆'
      }
    ]
  },
  {
    date: '2024/07/14',
    name: '粤西tho',
    place: '科尔顿国际酒店',
    href: 'https://map.baidu.com/search/%E7%A7%91%E5%B0%94%E9%A1%BF%E5%9B%BD%E9%99%85%E9%85%92%E5%BA%97/@12347254.635349732,2453697.5201736,19z?querytype=s&da_src=shareurl&wd=%E7%A7%91%E5%B0%94%E9%A1%BF%E5%9B%BD%E9%99%85%E9%85%92%E5%BA%97&c=194&src=0&pn=0&sug=0&l=18&b=(13154170.918391874,2790418.9647570653;13154906.81479072,2790763.2302623345)&from=webmap&biz_forward=%7B%22scaler%22:2,%22styles%22:%22pl%22%7D&device_ratio=2',
    details: [
      {
        identity: 'staff',
        others: '有缘相逢千里外，友人恰在此当中'
      }
    ]
  },
  {
    date: '2024/07/20',
    name: '深圳tho',
    place: '凯宾斯基酒店',
    href: 'https://map.baidu.com/search/%E6%B7%B1%E5%9C%B3%E5%87%AF%E5%AE%BE%E6%96%AF%E5%9F%BA%E9%85%92%E5%BA%97/@12684538.74,2558010.84,16z?querytype=s&da_src=shareurl&wd=%E5%87%AF%E5%AE%BE%E6%96%AF%E5%9F%BA%E9%85%92%E5%BA%97&c=340&src=0&pn=0&sug=0&l=13&b=(12274790,2396787;12315558,2415859)&from=webmap&biz_forward=%7B%22scaler%22:2,%22styles%22:%22pl%22%7D&device_ratio=2',
    details: [
      {
        identity: '摊主糕雨铺',
        others: '无言，但望周后，再赢夏归回'
      }
    ]
  },
  {
    date: '2024/07/28',
    name: '惠州thp',
    place: '维也纳酒店',
    href: 'https://map.baidu.com/search/%E7%BB%B4%E4%B9%9F%E7%BA%B3%E5%9B%BD%E9%99%85%E9%85%92%E5%BA%97(%E6%83%A0%E5%B7%9E%E6%B1%9F%E5%8C%97%E4%B8%89%E6%96%B0%E5%BA%97)/@12738242.585,2631351.87,19z?querytype=s&da_src=shareurl&wd=%E7%BB%B4%E4%B9%9F%E7%BA%B3%E5%9B%BD%E9%99%85%E9%85%92%E5%BA%97(%E6%83%A0%E5%B7%9E%E6%B1%9F%E5%8C%97%E4%B8%89%E6%96%B0%E5%BA%97)&c=139&src=0&wd2=%E6%83%A0%E5%B7%9E%E5%B8%82%E6%83%A0%E5%9F%8E%E5%8C%BA&pn=0&sug=1&l=19&b=(12346936.135349732,2453548.5201736;12347573.135349732,2453846.5201736)&from=webmap&biz_forward=%7B%22scaler%22:2,%22styles%22:%22pl%22%7D&sug_forward=56cf5a3babcf4433f4b91610&device_ratio=2',
    details: [
      {
        identity: '组委会',
        others: '行百里，孤回首，风起更落寞'
      }
    ]
  },
  {
    date: '2024/08/04',
    name: '潮汕tho',
    place: '123创意园',
    href: 'https://map.baidu.com/search/123%E5%88%9B%E6%84%8F%E5%9B%AD/@12957404.305,2681241.31,19z?querytype=s&da_src=shareurl&wd=123%E5%88%9B%E6%84%8F%E5%9B%AD&c=301&src=0&pn=0&sug=0&l=19&b=(12737924.085,2631202.87;12738561.085,2631500.87)&from=webmap&biz_forward=%7B%22scaler%22:2,%22styles%22:%22pl%22%7D&device_ratio=2',
    details: [
      {
        identity: '摊主西园',
        others: '情欲与阳烈'
      }
    ]
  },
  {
    date: '2024/08/10',
    name: '创建九制奇迹',
    place: '',
    href: '',
    details: [
      {
        identity: '共轭主催',
        others: 'qq群:963889675'
      }
    ]
  },
  {
    date: '2024/10/04',
    name: '南宁tho',
    place: '金御华尊国际大酒店',
    href: 'https://map.baidu.com/search/%E9%87%91%E5%BE%A1%E5%8D%8E%E5%B0%8A%E5%9B%BD%E9%99%85%E5%A4%A7%E9%85%92%E5%BA%97/@12058979.301131649,2599297.89348225,19z?querytype=s&da_src=shareurl&wd=%E9%87%91%E5%BE%A1%E5%8D%8E%E5%B0%8A%E5%9B%BD%E9%99%85%E5%A4%A7%E9%85%92%E5%BA%97&c=259&src=0&pn=0&sug=0&l=19&b=(12957085.805,2681092.31;12957722.805,2681390.31)&from=webmap&biz_forward=%7B%22scaler%22:2,%22styles%22:%22pl%22%7D&device_ratio=2',
    details: [
      {
        identity: '摊主九制奇迹',
        others: '满城百姓，感谢不尽'
      }
    ]
  }
]
</script>

<style scoped>
.demo-date-picker {
  display: flex;
  width: 100%;
  padding: 0;
  flex-wrap: wrap;
}
.el-link {
  margin-right: 8px;
  vertical-align: text-bottom;
}
.el-table-column {
  flex-shrink: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100px;
  height: 50px;
  margin: 10px;
  text-align: center;
  border-radius: 4px;
  background: var(--el-color-danger-light-9);
  color: var(--el-color-danger);
}
</style>
