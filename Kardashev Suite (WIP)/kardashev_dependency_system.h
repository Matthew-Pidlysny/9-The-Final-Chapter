/*
 * Kardashev Suite - Dependency Management System
 * Round 1: Foundation Implementation
 * 
 * Universal dependency system for Kardashev-level software components
 * Supports cross-language dependency resolution and management
 */

#ifndef KARDASHEV_DEPENDENCY_SYSTEM_H
#define KARDASHEV_DEPENDENCY_SYSTEM_H

#include "kardashev_file_types.h"
#include <string>
#include <vector>
#include <map>
#include <set>
#include <memory>
#include <functional>

namespace KardashevSuite {

/**
 * Programming Language Enumeration
 * Supported languages for Kardashev dependencies
 */
enum class ProgrammingLanguage {
    CPP,
    PYTHON,
    JAVA,
    CSHARP,
    JAVASCRIPT,
    RUST,
    GO,
    SWIFT,
    KOTLIN,
    TYPESCRIPT,
    UNKNOWN
};

/**
 * Dependency Version Information
 */
struct VersionInfo {
    uint32_t major;
    uint32_t minor;
    uint32_t patch;
    std::string pre_release;
    std::string build_metadata;
    
    VersionInfo(uint32_t maj = 1, uint32_t min = 0, uint32_t pat = 0)
        : major(maj), minor(min), patch(pat) {}
    
    std::string to_string() const;
    bool is_compatible_with(const VersionInfo& other) const;
    int compare_to(const VersionInfo& other) const;
};

/**
 * Dependency Specification
 */
struct DependencySpec {
    std::string name;
    VersionInfo version;
    ProgrammingLanguage language;
    KardashevLevel required_level;
    std::vector<std::string> features;
    std::map<std::string, std::string> properties;
    bool is_optional;
    
    DependencySpec() : language(ProgrammingLanguage::UNKNOWN), 
                      required_level(KardashevLevel::K1), 
                      is_optional(false) {}
};

/**
 * Dependency Resolution Result
 */
struct ResolutionResult {
    bool success;
    std::vector<DependencySpec> resolved_dependencies;
    std::vector<std::string> conflicts;
    std::vector<std::string> missing_dependencies;
    std::string error_message;
    
    ResolutionResult() : success(false) {}
};

/**
 * Abstract Dependency Resolver Interface
 */
class IDependencyResolver {
public:
    virtual ~IDependencyResolver() = default;
    virtual ResolutionResult resolve_dependencies(
        const std::vector<DependencySpec>& dependencies) = 0;
    virtual bool is_available(const DependencySpec& spec) = 0;
    virtual VersionInfo get_latest_version(const std::string& name) = 0;
};

/**
 * Package Repository Interface
 */
class IPackageRepository {
public:
    virtual ~IPackageRepository() = default;
    virtual bool contains_package(const std::string& name) = 0;
    virtual std::vector<VersionInfo> get_available_versions(const std::string& name) = 0;
    virtual DependencySpec get_package_spec(const std::string& name, const VersionInfo& version) = 0;
    virtual bool download_package(const DependencySpec& spec, const std::string& target_path) = 0;
};

/**
 * Language-Specific Package Manager
 */
class LanguagePackageManager {
public:
    virtual ~LanguagePackageManager() = default;
    virtual ProgrammingLanguage get_language() const = 0;
    virtual bool install_package(const DependencySpec& spec) = 0;
    virtual bool uninstall_package(const std::string& name) = 0;
    virtual bool is_package_installed(const std::string& name) = 0;
    virtual std::vector<std::string> list_installed_packages() = 0;
    virtual bool update_package(const std::string& name) = 0;
};

/**
 * Main Dependency Manager
 */
class KardashevDependencyManager {
private:
    std::map<ProgrammingLanguage, std::unique_ptr<LanguagePackageManager>> package_managers_;
    std::vector<std::unique_ptr<IPackageRepository>> repositories_;
    std::unique_ptr<IDependencyResolver> resolver_;
    
    // Cache for resolved dependencies
    std::map<std::string, ResolutionResult> resolution_cache_;
    
    // Configuration
    std::string cache_directory_;
    bool allow_downloads_;
    bool check_security_;
    
public:
    KardashevDependencyManager();
    ~KardashevDependencyManager();
    
    // Configuration
    void set_cache_directory(const std::string& path);
    void set_allow_downloads(bool allow);
    void set_check_security(bool check);
    
    // Repository management
    void add_repository(std::unique_ptr<IPackageRepository> repo);
    void remove_repository(const std::string& repo_name);
    
    // Package manager registration
    void register_package_manager(ProgrammingLanguage lang, 
                                 std::unique_ptr<LanguagePackageManager> manager);
    
    // Dependency resolution
    ResolutionResult resolve_dependencies(const std::vector<DependencySpec>& deps);
    ResolutionResult resolve_file_dependencies(const std::string& filepath);
    ResolutionResult resolve_project_dependencies(const std::string& project_path);
    
    // Installation management
    bool install_dependencies(const ResolutionResult& result);
    bool install_dependency(const DependencySpec& spec);
    bool uninstall_dependency(const std::string& name, ProgrammingLanguage lang);
    
    // Query operations
    std::vector<DependencySpec> get_installed_dependencies() const;
    std::vector<DependencySpec> get_dependencies_for_file(const std::string& filepath) const;
    bool is_satisfied(const DependencySpec& spec) const;
    
    // Validation
    bool validate_dependency_graph(const std::vector<DependencySpec>& deps);
    std::vector<std::string> find_circular_dependencies(const std::vector<DependencySpec>& deps);
    
    // Utility methods
    static ProgrammingLanguage detect_language_from_extension(const std::string& ext);
    static std::string language_to_string(ProgrammingLanguage lang);
    static ProgrammingLanguage string_to_language(const std::string& lang_str);
};

/**
 * Cross-Language Dependency Bridge
 * Allows dependencies from one language to be used in another
 */
class DependencyBridge {
public:
    struct BridgeSpec {
        ProgrammingLanguage source_lang;
        ProgrammingLanguage target_lang;
        std::string bridge_type;
        std::map<std::string, std::string> bridge_config;
    };
    
    virtual ~DependencyBridge() = default;
    virtual bool create_bridge(const DependencySpec& source, const BridgeSpec& bridge_spec) = 0;
    virtual bool is_bridge_available(const BridgeSpec& bridge_spec) = 0;
    virtual std::vector<BridgeSpec> get_available_bridges() = 0;
};

/**
 * Dependency Graph Visualizer
 */
class DependencyGraphVisualizer {
public:
    enum class OutputFormat {
        DOT,
        SVG,
        PNG,
        HTML,
        JSON
    };
    
    virtual ~DependencyGraphVisualizer() = default;
    virtual bool generate_graph(const std::vector<DependencySpec>& dependencies, 
                               const std::string& output_path, 
                               OutputFormat format) = 0;
    virtual bool generate_interactive_graph(const std::vector<DependencySpec>& dependencies,
                                           const std::string& output_path) = 0;
};

} // namespace KardashevSuite

#endif // KARDASHEV_DEPENDENCY_SYSTEM_H