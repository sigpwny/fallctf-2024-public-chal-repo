<script lang="ts">
	import type { PageServerData } from "./$types";

	export let data: PageServerData;
	let posts = data.posts;
</script>

<svelte:head>
	<title>Your Posts</title>
</svelte:head>

<div class="max-w-4xl mx-auto p-6">
  <div class="flex justify-between items-center mb-6">
    <h1 class="text-3xl font-bold">Posts</h1>
    <div class="space-x-4">
      <a 
        href="/logout"
        class="text-red-600 hover:text-red-800 font-medium"
      >
        Logout
      </a>

      <a 
        href="/create"
        class="bg-blue-600 text-white py-2 px-4 rounded hover:bg-blue-700"
      >
        Create New Post
      </a>
    </div>
  </div>

	{#if posts.length == 0}
		No posts!!! Create one above!
	{:else}
		{#each posts as post}
		<div class="bg-white rounded-lg shadow-lg p-6 mb-6 border border-gray-200">
			<h2 class="text-2xl font-bold text-gray-800 mb-2">{post.title}</h2>
			<p class="text-gray-600 mb-4">{post.content}</p>
		</div>
		{/each}
	{/if}
  
</div>



