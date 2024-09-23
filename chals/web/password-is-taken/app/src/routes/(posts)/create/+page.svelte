<script lang="ts">
	import { enhance } from "$app/forms";
	import type { ActionData } from "./$types";

	export let form: ActionData;
</script>

<svelte:head>
	<title>Add New Post</title>
</svelte:head>

{#if form?.error}
	{@html form?.message}
{/if}

<div class="max-w-4xl mx-auto p-6">
  <h1 class="text-3xl font-bold mb-6">Create New Post</h1>

  <form method="post" class="bg-white rounded-lg shadow-lg p-6 mb-6 border border-gray-200 space-y-6" enctype="multipart/form-data" use:enhance>
    
    <div>
      <label for="title" class="block text-lg font-medium text-gray-700">Title</label>
      <input 
        type="text" 
        id="title" 
        name="title" 
        class="mt-1 block w-full px-4 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm"
        placeholder="Enter your post title"
        required
      />
    </div>

    <div>
      <label for="content" class="block text-lg font-medium text-gray-700">Content</label>
      <textarea 
        id="content" 
        name="content" 
        rows="6" 
        required 
        class="mt-1 block w-full px-4 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm"
        placeholder="Enter your post content"
      ></textarea>
    </div>

    <div class="flex justify-end">
      <button 
        type="submit" 
        class="bg-blue-600 text-white py-2 px-6 rounded-lg hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2"
      >
        Submit
      </button>
    </div>
  </form>
</div>