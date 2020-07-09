<template>
  <div class="course">
    <h3 class="courseTitleFull">{{ courseTitleFull }}</h3>
	<p class="description"><strong>Description:</strong> {{ courseDetails }}</p>
	<p class="prerequisites"><strong>Prerequisites:</strong> {{ coursePrerequisites }}</p>
	<p class="tags"><strong>Tags:</strong> {{ tags }}</p>
  </div>
</template>

<script>
export default {
  name: 'Course',
  props: {
    courseTitleFull: String,
    courseDetails: String,
    coursePrerequisites: String,
    tags: String
  }
}
</script>

<style scoped>
.course{
  text-align: left;
  border: 1px solid gray;
  border-radius: 25px;
  margin: 20px;
  padding: 20px;
  width: 50%;
  
}
.courseTitleFull{
	color: #2c3e50;
}
.description{
  color: #2c3e50;
}
.prerequisites{
  color: #2c3e50;
}
.tags{
  color: #2c3e50;
}
</style>
