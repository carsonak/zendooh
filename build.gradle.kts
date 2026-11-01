import io.gitlab.arturbosch.detekt.Detekt
import org.jlleitschuh.gradle.ktlint.KtlintExtension

plugins {
    alias(libs.plugins.kotlin.multiplatform) apply false
    alias(libs.plugins.kotlin.android) apply false
    alias(libs.plugins.compose) apply false
    alias(libs.plugins.compose.compiler) apply false
    alias(libs.plugins.android.application) apply false
    alias(libs.plugins.android.kmp) apply false
    alias(libs.plugins.ktlint)
    alias(libs.plugins.detekt)
}

allprojects {
    apply(plugin = "org.jlleitschuh.gradle.ktlint")
    configure<KtlintExtension> {
        version.set(
            rootProject.libs.versions.ktlint.engine
                .get(),
        )
        filter {
            exclude("**/build/**", "**/generated/**", "**/vendor/**")
        }
    }
}

detekt {
    buildUponDefaultConfig = true
    config.setFrom(files("config/detekt.yml"))
}

// Analyze authored source across targets without a compiler/type-resolution classpath.
tasks.named<Detekt>("detekt") {
    setSource(fileTree(rootDir) { include("**/src/**/*.kt") })
    exclude("**/build/**", "**/generated/**", "**/vendor/**")
}
