@A = common global 
     [1024 x float]
     zeroinitializer, align 4
define i32 @main() nounwind {
<some initialization>
pollyBB:
  %insertInst = zext i1 true to i16
  %omp.userContext = alloca
     %main.omp_subfn.omp.userContext
  %0 = getelementptr inbounds
       %main.omp_subfn.omp.userContext*
       %omp.userContext, i32 0, i32 0
  store [1024 x float]*
        @A, [1024 x float]** %0
  call void 
      @GOMP_parallel_loop_runtime_start(
      void (i8*)* @main.omp_subfn,
      i8* %omp_data, i32 0, i32 0,
      i32 1024, i32 1)
  call void @main.omp_subfn(i8*%omp_data)
  call void @GOMP_parallel_end()
  br label %for.end12.region
}
